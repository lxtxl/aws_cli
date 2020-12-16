#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-action-histories.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # account-id : The account ID of the user. It should be a 12-digit number.
    # budget-name : A string that represents the budget name. The â:â and ââ characters arenât allowed.
    """

    execute_two_parameter("budgets", "describe-budget-action-histories", "account-id", "budget-name", parameter_display_string)