#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/set-identity-notification-topic.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # identity : The identity (email address or domain) that you want to set the Amazon SNS topic for.

Warning
You can only specify a verified identity for this parameter.

You can specify an identity by using its name or by using its Amazon Resource Name (ARN). The following examples are all valid identities: sender@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
    # notification-type : The type of notifications that will be published to the specified Amazon SNS topic.
Possible values:

Bounce
Complaint
Delivery
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ses", "set-identity-notification-topic", "identity", "notification-type", add_option_dict)
