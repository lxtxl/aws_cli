#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-identity-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/create-identity-pool.html
	describe-identity-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity-pool.html
	list-identity-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identity-pools.html
	update-identity-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/update-identity-pool.html
    """

    write_parameter("cognito-identity", "delete-identity-pool")