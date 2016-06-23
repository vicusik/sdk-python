from __future__ import unicode_literals
from lxml import etree, objectify

from . import apicontractsv1


class ApiResponse(object):
    namespaces = {'ns': 'AnetApi/xml/v1/schema/AnetApiSchema.xsd'}

    def __init__(self, xml_string):
        self.xml_string = xml_string
        self.root = etree.fromstring(xml_string, self.get_parser())
        # It is useless use apicontractsv1.CreateFromDocument to parse xml due bug inside parser
        # Note: objectify can't handle <text> tags, so <messages> should be processing by xpath
        self.api = objectify.fromstring(xml_string)

    @property
    def result_code(self):
        return self.root.xpath('//ns:resultCode/text()',
                               namespaces=self.namespaces)[0]

    def get_element_text(self, path, element=None):
        return (element or self.root).findtext(path, namespaces=self.namespaces)

    def get_element(self, path, element=None):
        return (element or self.root).xpath(path, namespaces=self.namespaces)

    def get_messages(self):
        """
        Return list of dictonaries with keys 'code', 'text'
        @return: list of dict
        """
        result = []
        messages = self.get_element('//ns:messages/ns:message')
        for message in messages:
            result.append(
                {'code': self.get_element_text('ns:code', message),
                 'text': self.get_element_text('ns:text', message)})
        return result

    @staticmethod
    def get_parser():
        return etree.XMLParser(
                ns_clean=True,
                no_network=True,
                encoding='utf-8',
                recover=True)
