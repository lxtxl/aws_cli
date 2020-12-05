#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-certificate.html
if __name__ == '__main__':
    """
	create-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-certificate.html
	get-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html
    """

    parameter_display_string = """
    # certificate-name : The name of the certificate to delete.
Use the GetCertificates action to get a list of certificate names that you can specify.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "delete-certificate", "certificate-name", add_option_dict)





