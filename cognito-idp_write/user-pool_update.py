#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-user-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool.html
	delete-user-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool.html
	describe-user-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool.html
	list-user-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pools.html
    """

    write_parameter("cognito-idp", "update-user-pool")