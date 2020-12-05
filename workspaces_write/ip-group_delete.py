#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-ip-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/associate-ip-groups.html
	create-ip-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-ip-group.html
	describe-ip-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-ip-groups.html
	disassociate-ip-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/disassociate-ip-groups.html
    """

    write_parameter("workspaces", "delete-ip-group")