#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/delete-resource-policy.html
	get-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/get-resource-policy.html
	put-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/put-resource-policy.html
    """

    write_parameter("secretsmanager", "validate-resource-policy")