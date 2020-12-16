#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-subscribers-for-notification.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # account-id : The accountId that is associated with the budget whose subscribers you want descriptions of.
    # budget-name : The name of the budget whose subscribers you want descriptions of.
    """

    execute_two_parameter("budgets", "describe-subscribers-for-notification", "account-id", "budget-name", parameter_display_string)