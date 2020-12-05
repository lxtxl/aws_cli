#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-policies.html
	list-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-identity-policies.html
	put-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/put-identity-policy.html
    """

    write_parameter("ses", "delete-identity-policy")