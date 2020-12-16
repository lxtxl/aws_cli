#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-identity-policy.html
	get-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-policies.html
	list-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-identity-policies.html
    """

    write_parameter("ses", "put-identity-policy")