#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-receipt-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-receipt-rule.html
	describe-receipt-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-receipt-rule.html
	update-receipt-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/update-receipt-rule.html
    """

    write_parameter("ses", "delete-receipt-rule")