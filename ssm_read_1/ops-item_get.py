#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-item.html
if __name__ == '__main__':
    """
	create-ops-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-ops-item.html
	describe-ops-items : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-ops-items.html
	update-ops-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-ops-item.html
    """

    parameter_display_string = """
    # ops-item-id : The ID of the OpsItem that you want to get.
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

    execute_one_parameter("ssm", "get-ops-item", "ops-item-id", add_option_dict)