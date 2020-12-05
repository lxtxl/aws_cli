#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-policy-versions.html
if __name__ == '__main__':
    """
	create-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-policy-version.html
	delete-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-policy-version.html
	get-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-policy-version.html
    """

    parameter_display_string = """
    # policy-name : The policy name.
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

    execute_one_parameter("iot", "list-policy-versions", "policy-name", add_option_dict)