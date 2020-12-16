#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-environment-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-membership.html
	delete-environment-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment-membership.html
	describe-environment-memberships : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environment-memberships.html
    """

    write_parameter("cloud9", "update-environment-membership")