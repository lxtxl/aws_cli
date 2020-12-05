#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-item.html
	get-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/get-item.html
	update-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-item.html
    """

    write_parameter("dynamodb", "put-item")