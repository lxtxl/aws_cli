#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/import-certificate.html
if __name__ == '__main__':
    """
	delete-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-certificate.html
	describe-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-certificates.html
    """

    parameter_display_string = """
    # certificate-identifier : A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They canât end with a hyphen or contain two consecutive hyphens.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dms", "import-certificate", "certificate-identifier", add_option_dict)





