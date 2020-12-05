#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/update-certificate-options.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # certificate-arn : ARN of the requested certificate to update. This must be of the form:

``arn:aws:acm:us-east-1:account :certificate/12345678-1234-1234-1234-123456789012 ``
    # options : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("acm", "update-certificate-options", "certificate-arn", "options", add_option_dict)
