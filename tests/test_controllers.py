import os
import unittest

from authorizenet import apicontractsv1
from authorizenet import apicontrollers

from factories.credit_card import CreditCard
from factories.order_factory import OrderFactory
from factories.customer import CustomerFactory


API_KEY = os.environ.get('API_KEY')
TRANSACTION_KEY = os.environ.get('TRANSACTION_KEY')


@unittest.skipIf(not API_KEY or not TRANSACTION_KEY, "No SandBox keys")
class TestSandboxAPIOperationBase(unittest.TestCase):
    def setUp(self):
        self.merchant = apicontractsv1.merchantAuthenticationType()
        self.merchant.name = API_KEY
        self.merchant.transactionKey = TRANSACTION_KEY

    def test_capture_transaction(self):
        credit_card = CreditCard()
        order = OrderFactory()

        card = apicontractsv1.creditCardType()
        card.cardNumber = credit_card['card_number']
        card.expirationDate = credit_card['expire_date'].strftime('%Y-%m')

        payment = apicontractsv1.paymentType()
        payment.creditCard = card

        transaction = apicontractsv1.transactionRequestType()
        transaction.transactionType = "authCaptureTransaction"
        transaction.amount = order['amount']
        transaction.payment = payment

        request = apicontractsv1.createTransactionRequest()
        request.merchantAuthentication = self.merchant
        request.refId = order['ref_id']
        request.transactionRequest = transaction

        controller = apicontrollers.CreateTransactionController(request)

        response = controller.execute()

        print(response)

    def test_create_customer_profile(self):
        """ Create customer profile and payment methods
        """
        customer = CustomerFactory()
        credit_card = CreditCard()

        profile = apicontractsv1.customerProfileType()
        profile.customerType = 'individual'
        profile.merchantCustomerId = customer['ref_id']
        profile.description = '%s %s' % (customer['first_name'], customer['last_name'])
        profile.email = customer['email']

        card = apicontractsv1.creditCardType()
        card.cardNumber = credit_card['card_number']
        card.expirationDate = credit_card['expire_date'].strftime('%Y-%m')

        payment = apicontractsv1.customerPaymentProfileType()
        payment.creditCard = card

        profile.paymentProfiles = [payment]

        create_profile_request = apicontractsv1.createCustomerProfileRequest()
        create_profile_request.merchantAuthentication = self.merchant
        create_profile_request.profile = profile

        controller = apicontrollers.CreateCustomerProfileController(create_profile_request)
        response = controller.execute()

        print(response)


