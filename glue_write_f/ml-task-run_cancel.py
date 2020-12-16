#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-ml-task-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-run.html
	get-ml-task-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-runs.html
    """

    write_parameter("glue", "cancel-ml-task-run")