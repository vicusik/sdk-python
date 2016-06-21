from __future__ import unicode_literals

import unittest
from authorizenet.response import ApiResponse


class TestFailureResponse(unittest.TestCase):
    def test_messages(self):
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
        response = ApiResponse(xml)

        self.assertEqual(response.result_code, 'Error')

        self.assertListEqual(response.get_messages(),
                             [{'code': 'E00029',
                               'text': 'Payment information is required.'}])
