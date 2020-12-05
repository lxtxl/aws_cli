#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deregister-workspace-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/deregister-workspace-directory.html
	describe-workspace-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-directories.html
    """

    write_parameter("workspaces", "register-workspace-directory")