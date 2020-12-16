#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	clone-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/clone-receipt-rule-set.html
	create-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-receipt-rule-set.html
	describe-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-receipt-rule-set.html
	list-receipt-rule-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-receipt-rule-sets.html
	reorder-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/reorder-receipt-rule-set.html
    """

    write_parameter("ses", "delete-receipt-rule-set")