#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-mount-target-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-mount-target-security-groups.html
    """

    write_parameter("efs", "modify-mount-target-security-groups")