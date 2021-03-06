#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-backup.html
	describe-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-backup.html
	list-backups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-backups.html
    """

    write_parameter("dynamodb", "delete-backup")