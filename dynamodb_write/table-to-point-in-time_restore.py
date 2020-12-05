#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	export-table-to-point-in-time : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/export-table-to-point-in-time.html
    """

    write_parameter("dynamodb", "restore-table-to-point-in-time")