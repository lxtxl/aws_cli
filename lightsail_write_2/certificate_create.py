#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-certificate.html
if __name__ == '__main__':
    """
	delete-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-certificate.html
	get-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html
    """

    parameter_display_string = """
    # certificate-name : The name for the certificate.
    # domain-name : The domain name (e.g., example.com ) for the certificate.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "create-certificate", "certificate-name", "domain-name", add_option_dict)
