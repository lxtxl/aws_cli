#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/set-identity-feedback-forwarding-enabled.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # identity : The identity for which to set bounce and complaint notification forwarding. Examples: user@example.com , example.com .
    # forwarding-enabled | --no-forwarding-enabled : Sets whether Amazon SES will forward bounce and complaint notifications as email. true specifies that Amazon SES will forward bounce and complaint notifications as email, in addition to any Amazon SNS topic publishing otherwise specified. false specifies that Amazon SES will publish bounce and complaint notifications only through Amazon SNS. This value can only be set to false when Amazon SNS topics are set for both Bounce and Complaint notification types.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ses", "set-identity-feedback-forwarding-enabled", "identity", "forwarding-enabled | --no-forwarding-enabled", add_option_dict)
