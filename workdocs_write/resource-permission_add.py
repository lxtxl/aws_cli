#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-resource-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-resource-permissions.html
	remove-resource-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/remove-resource-permission.html
    """

    write_parameter("workdocs", "add-resource-permissions")