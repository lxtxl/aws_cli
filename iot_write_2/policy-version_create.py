#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-policy-version.html
if __name__ == '__main__':
    """
	delete-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-policy-version.html
	get-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-policy-version.html
	list-policy-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-policy-versions.html
    """

    parameter_display_string = """
    # policy-name : The policy name.
    # policy-document : The JSON document that describes the policy. Minimum length of 1. Maximum length of 2048, excluding whitespace.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "create-policy-version", "policy-name", "policy-document", add_option_dict)
