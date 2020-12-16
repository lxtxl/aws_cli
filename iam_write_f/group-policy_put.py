#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-group-policy.html
	delete-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group-policy.html
	detach-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-group-policy.html
	get-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group-policy.html
	list-group-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-group-policies.html
    """

    write_parameter("iam", "put-group-policy")