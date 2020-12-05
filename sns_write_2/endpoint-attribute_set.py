#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-endpoint-attributes.html
if __name__ == '__main__':
    """
	get-endpoint-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-endpoint-attributes.html
    """

    parameter_display_string = """
    # endpoint-arn : EndpointArn used for SetEndpointAttributes action.
    # attributes : A map of the endpoint attributes. Attributes in this map include the following:

CustomUserData â arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
Enabled â flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.
Token â device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.

key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sns", "set-endpoint-attributes", "endpoint-arn", "attributes", add_option_dict)
