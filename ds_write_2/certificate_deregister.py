#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/deregister-certificate.html
if __name__ == '__main__':
    """
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-certificates.html
	register-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/register-certificate.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory.
    # certificate-id : The identifier of the certificate.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "deregister-certificate", "directory-id", "certificate-id", add_option_dict)
