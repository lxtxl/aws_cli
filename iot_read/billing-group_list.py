#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-billing-groups.html
if __name__ == '__main__':
    """
	create-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-billing-group.html
	delete-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-billing-group.html
	describe-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-billing-group.html
	update-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-billing-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("iot", "list-billing-groups", add_option_dict)