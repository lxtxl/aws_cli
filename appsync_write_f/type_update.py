#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html
	delete-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-type.html
	get-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-type.html
	list-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-types.html
    """

    write_parameter("appsync", "update-type")