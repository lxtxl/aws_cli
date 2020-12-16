#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-notification.html
if __name__ == '__main__':
    """
	create-notification : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-notification.html
	update-notification : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-notification.html
    """

    parameter_display_string = """
    # account-id : The accountId that is associated with the budget whose notification you want to delete.
    # budget-name : The name of the budget whose notification you want to delete.
    # notification : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("budgets", "delete-notification", "account-id", "budget-name", "notification", add_option_dict)
