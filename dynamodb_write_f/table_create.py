#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-table.html
	describe-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-table.html
	list-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-tables.html
	update-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-table.html
    """

    write_parameter("dynamodb", "create-table")