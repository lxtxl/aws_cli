#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-budget-action.html
if __name__ == '__main__':
    """
	create-budget-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget-action.html
	describe-budget-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-action.html
	execute-budget-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/execute-budget-action.html
	update-budget-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-budget-action.html
    """

    parameter_display_string = """
    # account-id : The account ID of the user. It should be a 12-digit number.
    # budget-name : A string that represents the budget name. The â:â and ââ characters arenât allowed.
    # action-id : A system-generated universally unique identifier (UUID) for the action.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("budgets", "delete-budget-action", "account-id", "budget-name", "action-id", add_option_dict)
