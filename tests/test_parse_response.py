from __future__ import unicode_literals

import unittest
from lxml import etree, objectify

from authorizenet import apicontractsv1


class TestParseFailureResponse(unittest.TestCase):
    def test_xml_parser(self):
        xml = b"""<?xml version="1.0" encoding="utf-8"?>
        <createCustomerProfileResponse xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
            <messages>
                <resultCode>Ok</resultCode>
                <message>
                    <code>I00001</code>
                    <text>Successful.</text>
                </message>
            </messages>
            <customerProfileId>41049270</customerProfileId>
            <customerPaymentProfileIdList>
                <numericString>37347079</numericString>
                <numericString>37347080</numericString>
            </customerPaymentProfileIdList>
            <customerShippingAddressIdList/>
            <validationDirectResponseList/>
        </createCustomerProfileResponse>"""
        xml_object = apicontractsv1.CreateFromDocument(xml, 'AnetApi/xml/v1/schema/AnetApiSchema.xsd')
        xml2_object = objectify.fromstring(xml)
        print xml_object


    def test_profile_response(self):
        """ Reference XML parsing code for controllers
        """

        xml = b"""<?xml version="1.0" encoding="utf-8"?>
        <createCustomerProfileResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
            <messages>
                <resultCode>Error</resultCode>
                <message>
                    <code>E00029</code>
                    <text>Payment information is required.</text>
                </message>
            </messages>
            <customerPaymentProfileIdList />
            <customerShippingAddressIdList />
            <validationDirectResponseList />
        </createCustomerProfileResponse>"""

        parser = etree.XMLParser(ns_clean=True,
                                 no_network=True,
                                 encoding='utf-8',
                                 recover=True)
        root = etree.fromstring(xml, parser)
        namespaces = {'ns': 'AnetApi/xml/v1/schema/AnetApiSchema.xsd'}

        result_code = root.xpath('//ns:resultCode/text()', namespaces=namespaces)
        self.assertEqual(result_code, 'Error')
        messages = root.xpath('//ns:messages/ns:message', namespaces=namespaces)

        message = messages[0]

        code = message.findtext('ns:code', namespaces={'ns': 'AnetApi/xml/v1/schema/AnetApiSchema.xsd'})
        text = message.findtext('ns:text', namespaces={'ns': 'AnetApi/xml/v1/schema/AnetApiSchema.xsd'})

        self.assertEqual(code, 'E00029')
        self.assertEqual(text, 'Payment information is required.')
