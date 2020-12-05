#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-export-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-export-tasks.html
	start-export-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-export-task.html
    """

    write_parameter("rds", "cancel-export-task")