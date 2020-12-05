#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/get-resource-policy.html
	put-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/put-resource-policy.html
	validate-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/validate-resource-policy.html
    """

    write_parameter("secretsmanager", "delete-resource-policy")