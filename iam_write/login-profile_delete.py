#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-login-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-login-profile.html
	get-login-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html
	update-login-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-login-profile.html
    """

    write_parameter("iam", "delete-login-profile")