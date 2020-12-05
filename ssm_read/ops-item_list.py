#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-ops-items.html
if __name__ == '__main__':
    """
	create-ops-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-ops-item.html
	get-ops-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-item.html
	update-ops-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-ops-item.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("ssm", "describe-ops-items", add_option_dict)