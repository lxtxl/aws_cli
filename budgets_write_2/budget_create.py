#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget.html
if __name__ == '__main__':
    """
	delete-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-budget.html
	describe-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget.html
	describe-budgets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budgets.html
	update-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-budget.html
    """

    parameter_display_string = """
    # account-id : The accountId that is associated with the budget.
    # budget : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("budgets", "create-budget", "account-id", "budget", add_option_dict)
