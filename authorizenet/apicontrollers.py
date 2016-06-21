"""
Created on Nov 19, 2015

@author: krgupta
"""

from .constants import constants
from . import apicontractsv1
from apicontrollersbase import APIOperationBase


class ARBCancelSubscriptionController(APIOperationBase):
    request_type = 'ARBCancelSubscriptionRequest'
    response_class = apicontractsv1.ARBCancelSubscriptionResponse


class ARBCreateSubscriptionController(APIOperationBase):
    request_type = 'ARBCreateSubscriptionRequest'
    response_class = apicontractsv1.ARBCreateSubscriptionResponse


class ARBGetSubscriptionController(APIOperationBase):
    request_type = 'ARBGetSubscriptionRequest'
    response_class = apicontractsv1.ARBGetSubscriptionResponse


class ARBGetSubscriptionListController(APIOperationBase):
    request_type = 'ARBGetSubscriptionListRequest'
    response_class = apicontractsv1.ARBGetSubscriptionListResponse


class ARBGetSubscriptionStatusController(APIOperationBase):
    request_type = 'ARBGetSubscriptionStatusRequest'
    response_class = apicontractsv1.ARBGetSubscriptionStatusResponse

    def afterexecute(self, response):
        response = self._httpResponse
        if constants.note in response:
            response = response.replace(constants.note, '')

        if constants.StatusStart in response:
            start = response.index(constants.StatusStart)
            end = response.index(constants.StatusEnd)
            response = response.replace(response[start:end+9], '')
        return response


class ARBUpdateSubscriptionController(APIOperationBase):
    request_type = 'ARBUpdateSubscriptionRequest'
    response_class = apicontractsv1.ARBUpdateSubscriptionResponse


class AuthenticateTestController(APIOperationBase):
    request_type = 'authenticateTestRequest'
    response_class = apicontractsv1.authenticateTestResponse


class CreateCustomerPaymentProfileController(APIOperationBase):
    request_type = 'createCustomerPaymentProfileRequest'
    response_class = apicontractsv1.createCustomerPaymentProfileResponse


class CreateCustomerProfileController(APIOperationBase):
    request_type = 'createCustomerProfileRequest'
    response_class = apicontractsv1.createCustomerProfileResponse


class CreateCustomerProfileFromTransactionController(APIOperationBase):
    request_type = 'createCustomerProfileFromTransactionRequest'
    response_class = apicontractsv1.createCustomerProfileResponse


class CreateCustomerProfileTransactionController(APIOperationBase):
    request_type = 'createCustomerProfileTransactionRequest'
    response_class = apicontractsv1.createCustomerProfileTransactionResponse


class CreateCustomerShippingAddressController(APIOperationBase):
    request_type = 'createCustomerShippingAddressRequest'
    response_class = apicontractsv1.createCustomerShippingAddressResponse


class CreateTransactionController(APIOperationBase):
    request_type = 'createTransactionRequest'
    response_class = apicontractsv1.createTransactionResponse


class DecryptPaymentDataController(APIOperationBase):
    request_type = 'decryptPaymentDataRequest'
    response_class = apicontractsv1.decryptPaymentDataResponse


class DeleteCustomerPaymentProfileController(APIOperationBase):
    request_type = 'deleteCustomerPaymentProfileRequest'
    response_class = apicontractsv1.deleteCustomerPaymentProfileResponse


class DeleteCustomerProfileController(APIOperationBase):
    request_type = 'deleteCustomerProfileRequest'
    response_class = apicontractsv1.deleteCustomerProfileResponse


class DeleteCustomerShippingAddressController(APIOperationBase):
    request_type = 'deleteCustomerShippingAddressRequest'
    response_class = apicontractsv1.deleteCustomerShippingAddressResponse


class ErrorController(APIOperationBase):
    request_type = 'ErrorRequest'
    response_class = apicontractsv1.ErrorResponse


class GetBatchStatisticsController(APIOperationBase):
    request_type = 'getBatchStatisticsRequest'
    response_class = apicontractsv1.getBatchStatisticsResponse


class GetCustomerPaymentProfileController(APIOperationBase):
    request_type = 'getCustomerPaymentProfileRequest'
    response_class = apicontractsv1.getCustomerPaymentProfileResponse


class GetCustomerPaymentProfileListController(APIOperationBase):
    request_type = 'getCustomerPaymentProfileListRequest'
    response_class = apicontractsv1.getCustomerPaymentProfileListResponse


class GetCustomerProfileController(APIOperationBase):
    request_type = 'getCustomerProfileRequest'
    response_class = apicontractsv1.getCustomerProfileResponse


class GetCustomerProfileIdsController(APIOperationBase):
    request_type = 'getCustomerProfileIdsRequest'
    response_class = apicontractsv1.getCustomerProfileIdsResponse


class GetCustomerShippingAddressController(APIOperationBase):
    request_type = 'getCustomerShippingAddressRequest'
    response_class = apicontractsv1.getCustomerShippingAddressResponse


class GetHostedProfilePageController(APIOperationBase):
    request_type = 'getHostedProfilePageRequest'
    response_class = apicontractsv1.getHostedProfilePageResponse


class GetSettledBatchListController(APIOperationBase):
    request_type = 'getSettledBatchListRequest'
    response_class = apicontractsv1.getSettledBatchListResponse


class GetTransactionDetailsController(APIOperationBase):
    request_type = 'getTransactionDetailsRequest'
    response_class = apicontractsv1.getTransactionDetailsResponse


class GetTransactionListController(APIOperationBase):
    request_type = 'getTransactionListRequest'
    response_class = apicontractsv1.getTransactionListResponse


class GetUnsettledTransactionListController(APIOperationBase):
    request_type = 'getUnsettledTransactionListRequest'
    response_class = apicontractsv1.getUnsettledTransactionListResponse


class IsAliveController(APIOperationBase):
    request_type = 'isAliveRequest'
    response_class = apicontractsv1.isAliveResponse


class LogoutController(APIOperationBase):
    request_type = 'logoutRequest'
    response_class = apicontractsv1.logoutResponse


class MobileDeviceLoginController(APIOperationBase):
    request_type = 'mobileDeviceLoginRequest'
    response_class = apicontractsv1.mobileDeviceLoginResponse


class MobileDeviceRegistrationController(APIOperationBase):
    request_type = 'mobileDeviceRegistrationRequest'
    response_class = apicontractsv1.mobileDeviceRegistrationResponse


class SendCustomerTransactionReceiptController(APIOperationBase):
    request_type = 'sendCustomerTransactionReceiptRequest'
    response_class = apicontractsv1.sendCustomerTransactionReceiptResponse


class UpdateCustomerPaymentProfileController(APIOperationBase):
    request_type = 'updateCustomerPaymentProfileRequest'
    response_class = apicontractsv1.updateCustomerPaymentProfileResponse


class UpdateCustomerProfileController(APIOperationBase):
    request_type = 'updateCustomerProfileRequest'
    response_class = apicontractsv1.updateCustomerProfileResponse


class UpdateCustomerShippingAddressController(APIOperationBase):
    request_type = 'updateCustomerShippingAddressRequest'
    response_class = apicontractsv1.updateCustomerShippingAddressResponse


class UpdateSplitTenderGroupController(APIOperationBase):
    request_type = 'updateSplitTenderGroupRequest'
    response_class = apicontractsv1.updateSplitTenderGroupResponse


class ValidateCustomerPaymentProfileController(APIOperationBase):
    request_type = 'validateCustomerPaymentProfileRequest'
    response_class = apicontractsv1.validateCustomerPaymentProfileResponse
