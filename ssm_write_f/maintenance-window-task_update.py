#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-maintenance-window-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-tasks.html
	get-maintenance-window-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-task.html
    """

    write_parameter("ssm", "update-maintenance-window-task")