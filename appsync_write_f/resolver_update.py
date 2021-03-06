#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-resolver : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-resolver.html
	delete-resolver : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-resolver.html
	get-resolver : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-resolver.html
	list-resolvers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-resolvers.html
    """

    write_parameter("appsync", "update-resolver")