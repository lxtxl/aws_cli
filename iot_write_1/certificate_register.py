#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-certificate.html
if __name__ == '__main__':
    """
	delete-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-certificate.html
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-certificates.html
	transfer-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/transfer-certificate.html
	update-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html
    """

    parameter_display_string = """
    # certificate-pem : The certificate data, in PEM format.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "register-certificate", "certificate-pem", add_option_dict)





