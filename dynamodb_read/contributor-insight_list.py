#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-contributor-insights.html
if __name__ == '__main__':
    """
	describe-contributor-insights : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-contributor-insights.html
	update-contributor-insights : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-contributor-insights.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("dynamodb", "list-contributor-insights", add_option_dict)