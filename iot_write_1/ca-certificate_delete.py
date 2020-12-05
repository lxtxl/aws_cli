#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-ca-certificate.html
if __name__ == '__main__':
    """
	describe-ca-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html
	list-ca-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-ca-certificates.html
	register-ca-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-ca-certificate.html
	update-ca-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-ca-certificate.html
    """

    parameter_display_string = """
    # certificate-id : The ID of the certificate to delete. (The last part of the certificate ARN contains the certificate ID.)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "delete-ca-certificate", "certificate-id", add_option_dict)





