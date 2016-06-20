"""
Created on Nov 1, 2015

@author: krgupta
"""

import logging
import xml.dom.minidom
import requests
from lxml import etree

from . import constants
from . import apicontractsv1
from . import utility
from .exceptions import AuthorizeTransactionFailure, AuthorizeResponseFailure


logger = logging.getLogger('authorizenet')


class APIOperationBase(object):
    request_type = None
    response_class = None

    _merchantauthentication = apicontractsv1.merchantAuthenticationType()

    def __init__(self, api_request, production_mode=False):
        self._request = api_request
        self.endpoint = constants.PRODUCTION if production_mode else constants.SANDBOX

        # objectify variables
        self._responseXML = None
        self._responseObject = None
        self._mainObject = None

    def buildrequest(self):
        xml_request = self._request.toxml(encoding='utf-8',
                                          element_name=self.request_type)

        # remove namespaces that toxml() generates
        xml_request = xml_request.replace('ns1:', '')
        xml_request = xml_request.replace(':ns1', '')
        return xml_request

    @staticmethod
    def get_pretty_xml(xml_data):
        dom_obj = xml.dom.minidom.parseString(xml_data)
        return dom_obj.toprettyxml()
    
    def execute(self):
        proxy_data = {'http': utility.helper.getproperty("http"),
                      'https': utility.helper.getproperty("https"),
                      'ftp': utility.helper.getproperty("ftp")}
                           
        # requests is http request
        xml_request = self.buildrequest()

        logger.debug('Executing http post to url: %s, request=%s', self.endpoint, xml_request)

        try:
            response = requests.post(
                self.endpoint,
                data=xml_request,
                headers={'Content-Type': 'application/xml',
                         'version': '1.0',
                         'encoding': 'utf-8'},
                proxies=proxy_data)
        except Exception:
            logger.error('Error retrieving http response from: %s for request: %s',
                         self.endpoint,
                         self.get_pretty_xml(xml_request))
            raise

        parser = etree.XMLParser(
                ns_clean=True,
                no_network=True,
                encoding='utf-8',
                recover=True)

        if response.status_code != 200:
            logger.error("Authorize.net gateway response code %d", response.status_code)
            raise AuthorizeResponseFailure(response)

        root = etree.fromstring(response.content, parser)
        namespaces = {'ns': 'AnetApi/xml/v1/schema/AnetApiSchema.xsd'}
        result_code = root.xpath('//ns:resultCode/text()', namespaces=namespaces)[0]

        if result_code != constants.RESULT_SUCCESS:
            # FIXME: at the moment finding only first error code
            messages = root.xpath('//ns:messages/ns:message', namespaces=namespaces)
            message = messages[0]
            code = message.findtext('ns:code', namespaces=namespaces)
            text = message.findtext('ns:text', namespaces=namespaces)
            raise AuthorizeTransactionFailure(code, text)

        response_object = apicontractsv1.CreateFromDocument(response.content)

        return response_object
