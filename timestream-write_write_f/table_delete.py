#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-table.html
	describe-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/describe-table.html
	list-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/list-tables.html
	update-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/update-table.html
    """

    write_parameter("timestream-write", "delete-table")