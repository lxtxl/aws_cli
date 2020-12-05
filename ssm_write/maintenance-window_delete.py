#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-maintenance-window.html
	describe-maintenance-windows : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-windows.html
	get-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window.html
	update-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window.html
    """

    write_parameter("ssm", "delete-maintenance-window")