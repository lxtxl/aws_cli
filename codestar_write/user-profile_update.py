#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/create-user-profile.html
	delete-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/delete-user-profile.html
	describe-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/describe-user-profile.html
	list-user-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-user-profiles.html
    """

    write_parameter("codestar", "update-user-profile")