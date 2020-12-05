#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-api-key.html
	list-api-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-api-keys.html
	update-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-api-key.html
    """

    write_parameter("appsync", "create-api-key")