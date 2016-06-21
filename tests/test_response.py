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

    def test_create_profile_response(self):
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
        response = ApiResponse(xml)

        self.assertEqual(response.result_code, 'Ok')
        self.assertEqual(response.api.customerProfileId, 41049270)
        self.assertListEqual(list(response.api.customerPaymentProfileIdList.numericString),
                             [37347079, 37347080])
