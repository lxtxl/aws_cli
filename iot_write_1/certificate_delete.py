#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-certificate.html
if __name__ == '__main__':
    """
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-certificates.html
	register-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-certificate.html
	transfer-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/transfer-certificate.html
	update-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html
    """

    parameter_display_string = """
    # certificate-id : The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "delete-certificate", "certificate-id", add_option_dict)





