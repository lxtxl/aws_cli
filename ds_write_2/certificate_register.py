#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/register-certificate.html
if __name__ == '__main__':
    """
	deregister-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/deregister-certificate.html
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-certificates.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory.
    # certificate-data : The certificate PEM string that needs to be registered.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "register-certificate", "directory-id", "certificate-data", add_option_dict)
