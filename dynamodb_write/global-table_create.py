#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-global-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-global-table.html
	list-global-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-global-tables.html
	update-global-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-global-table.html
    """

    write_parameter("dynamodb", "create-global-table")