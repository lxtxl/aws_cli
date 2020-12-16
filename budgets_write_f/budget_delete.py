#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget.html
	describe-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget.html
	describe-budgets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budgets.html
	update-budget : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-budget.html
    """

    write_parameter("budgets", "delete-budget")