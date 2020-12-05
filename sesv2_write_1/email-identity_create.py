#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-email-identity.html
if __name__ == '__main__':
    """
	delete-email-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-email-identity.html
	get-email-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-email-identity.html
	list-email-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-email-identities.html
    """

    parameter_display_string = """
    # email-identity : The email address or domain that you want to verify.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sesv2", "create-email-identity", "email-identity", add_option_dict)





