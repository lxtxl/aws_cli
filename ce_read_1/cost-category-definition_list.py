#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/describe-cost-category-definition.html
if __name__ == '__main__':
    """
	create-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-cost-category-definition.html
	delete-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-cost-category-definition.html
	list-cost-category-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-category-definitions.html
	update-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-cost-category-definition.html
    """

    parameter_display_string = """
    # cost-category-arn : The unique identifier for your Cost Category.
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

    execute_one_parameter("ce", "describe-cost-category-definition", "cost-category-arn", add_option_dict)