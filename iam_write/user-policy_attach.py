#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-policy.html
	detach-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-user-policy.html
	get-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user-policy.html
	list-user-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-policies.html
	put-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-policy.html
    """

    write_parameter("iam", "attach-user-policy")