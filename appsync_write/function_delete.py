#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-function.html
	get-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-function.html
	list-functions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-functions.html
	update-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-function.html
    """

    write_parameter("appsync", "delete-function")