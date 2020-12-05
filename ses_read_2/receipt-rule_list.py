#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-receipt-rule.html
if __name__ == '__main__':
    """
	create-receipt-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-receipt-rule.html
	delete-receipt-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-receipt-rule.html
	update-receipt-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/update-receipt-rule.html
    """

    parameter_display_string = """
    # rule-set-name : The name of the receipt rule set that the receipt rule belongs to.
    # rule-name : The name of the receipt rule.
    """

    execute_two_parameter("ses", "describe-receipt-rule", "rule-set-name", "rule-name", parameter_display_string)