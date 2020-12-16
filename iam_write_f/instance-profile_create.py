#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-instance-profile.html
	get-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-instance-profile.html
	list-instance-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-instance-profiles.html
    """

    write_parameter("iam", "create-instance-profile")