#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget.html
if __name__ == '__main__':
    """
	create-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget.html
	delete-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-budget.html
	describe-budgets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budgets.html
	update-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-budget.html
    """

    parameter_display_string = """
    # account-id : The accountId that is associated with the budget that you want a description of.
    # budget-name : The name of the budget that you want a description of.
    """

    execute_two_parameter("budgets", "describe-budget", "account-id", "budget-name", parameter_display_string)