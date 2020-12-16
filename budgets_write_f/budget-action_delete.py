#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-budget-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget-action.html
	describe-budget-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-action.html
	execute-budget-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/execute-budget-action.html
	update-budget-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-budget-action.html
    """

    write_parameter("budgets", "delete-budget-action")