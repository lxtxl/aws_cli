#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-cost-category-definition.html
if __name__ == '__main__':
    """
	create-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-cost-category-definition.html
	describe-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/describe-cost-category-definition.html
	list-cost-category-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-category-definitions.html
	update-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-cost-category-definition.html
    """

    parameter_display_string = """
    # cost-category-arn : The unique identifier for your Cost Category.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ce", "delete-cost-category-definition", "cost-category-arn", add_option_dict)





