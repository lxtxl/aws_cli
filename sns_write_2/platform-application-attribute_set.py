#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-platform-application-attributes.html
if __name__ == '__main__':
    """
	get-platform-application-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-platform-application-attributes.html
    """

    parameter_display_string = """
    # platform-application-arn : PlatformApplicationArn for SetPlatformApplicationAttributes action.
    # attributes : A map of the platform application attributes. Attributes in this map include the following:

PlatformCredential â The credential received from the notification service. For APNS and APNS_SANDBOX , PlatformCredential is private key . For GCM (Firebase Cloud Messaging), PlatformCredential is API key . For ADM , PlatformCredential is client secret .
PlatformPrincipal â The principal received from the notification service. For APNS and APNS_SANDBOX , PlatformPrincipal is SSL certificate . For GCM (Firebase Cloud Messaging), there is no PlatformPrincipal . For ADM , PlatformPrincipal is client id .
EventEndpointCreated â Topic ARN to which EndpointCreated event notifications are sent.
EventEndpointDeleted â Topic ARN to which EndpointDeleted event notifications are sent.
EventEndpointUpdated â Topic ARN to which EndpointUpdate event notifications are sent.
EventDeliveryFailure â Topic ARN to which DeliveryFailure event notifications are sent upon Direct Publish delivery failure (permanent) to one of the applicationâs endpoints.
SuccessFeedbackRoleArn â IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
FailureFeedbackRoleArn â IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
SuccessFeedbackSampleRate â Sample rate percentage (0-100) of successfully delivered messages.

key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sns", "set-platform-application-attributes", "platform-application-arn", "attributes", add_option_dict)
