#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-parameter-groups.html
if __name__ == '__main__':
    """
	create-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/create-parameter-group.html
	delete-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-parameter-group.html
	update-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/update-parameter-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("dax", "describe-parameter-groups", add_option_dict)