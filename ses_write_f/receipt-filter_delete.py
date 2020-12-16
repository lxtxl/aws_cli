#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-receipt-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-receipt-filter.html
	list-receipt-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-receipt-filters.html
    """

    write_parameter("ses", "delete-receipt-filter")