#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-email-identity-policies.html
if __name__ == '__main__':
    """
	create-email-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-email-identity-policy.html
	delete-email-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-email-identity-policy.html
	update-email-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-email-identity-policy.html
    """

    parameter_display_string = """
    # email-identity : The email identity that you want to retrieve policies for.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("sesv2", "get-email-identity-policies", "email-identity", add_option_dict)