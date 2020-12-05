#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-input-security-group.html
if __name__ == '__main__':
    """
	create-input-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-input-security-group.html
	delete-input-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-input-security-group.html
	list-input-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-security-groups.html
	update-input-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-input-security-group.html
    """

    parameter_display_string = """
    # input-security-group-id : The id of the Input Security Group to describe
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

    execute_one_parameter("medialive", "describe-input-security-group", "input-security-group-id", add_option_dict)