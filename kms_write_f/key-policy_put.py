#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-key-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-key-policy.html
	list-key-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-key-policies.html
    """

    write_parameter("kms", "put-key-policy")