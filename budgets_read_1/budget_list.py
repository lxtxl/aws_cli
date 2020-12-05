#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budgets.html
if __name__ == '__main__':
    """
	create-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget.html
	delete-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-budget.html
	describe-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget.html
	update-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-budget.html
    """

    parameter_display_string = """
    # account-id : The accountId that is associated with the budgets that you want descriptions of.
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

    execute_one_parameter("budgets", "describe-budgets", "account-id", add_option_dict)