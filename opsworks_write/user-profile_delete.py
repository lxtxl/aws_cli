#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-user-profile.html
	describe-user-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-user-profiles.html
	update-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-user-profile.html
    """

    write_parameter("opsworks", "delete-user-profile")