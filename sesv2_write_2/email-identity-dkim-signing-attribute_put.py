#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/put-email-identity-dkim-signing-attributes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # email-identity : The email identity that you want to configure DKIM for.
    # signing-attributes-origin : The method that you want to use to configure DKIM for the identity. There are two possible values:

AWS_SES â Configure DKIM for the identity by using Easy DKIM .
EXTERNAL â Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM).

Possible values:

AWS_SES
EXTERNAL
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sesv2", "put-email-identity-dkim-signing-attributes", "email-identity", "signing-attributes-origin", add_option_dict)
