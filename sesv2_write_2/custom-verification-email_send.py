#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/send-custom-verification-email.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # email-address : The email address to verify.
    # template-name : The name of the custom verification email template to use when sending the verification email.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sesv2", "send-custom-verification-email", "email-address", "template-name", add_option_dict)
