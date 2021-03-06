#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html
	delete-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role-policy.html
	detach-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-role-policy.html
	get-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role-policy.html
	list-role-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-role-policies.html
    """

    write_parameter("iam", "put-role-policy")