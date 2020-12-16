#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-data-repository-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/cancel-data-repository-task.html
	describe-data-repository-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-data-repository-tasks.html
    """

    write_parameter("fsx", "create-data-repository-task")