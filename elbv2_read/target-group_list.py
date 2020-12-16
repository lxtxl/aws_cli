#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-groups.html
if __name__ == '__main__':
    """
	create-target-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-target-group.html
	delete-target-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-target-group.html
	modify-target-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("elbv2", "describe-target-groups", add_option_dict)