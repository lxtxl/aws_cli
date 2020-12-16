#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-target-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-target-group.html
	delete-target-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-target-group.html
	describe-target-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-groups.html
    """

    write_parameter("elbv2", "modify-target-group")