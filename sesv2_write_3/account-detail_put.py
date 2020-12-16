#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/put-account-details.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # mail-type : The type of email your account will send.
Possible values:

MARKETING
TRANSACTIONAL
    # website-url : The URL of your website. This information helps us better understand the type of content that you plan to send.
    # use-case-description : A description of the types of email that you plan to send.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sesv2", "put-account-details", "mail-type", "website-url", "use-case-description", add_option_dict)
