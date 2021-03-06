#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-database.html
	delete-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/delete-database.html
	describe-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/describe-database.html
	list-databases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/list-databases.html
    """

    write_parameter("timestream-write", "update-database")