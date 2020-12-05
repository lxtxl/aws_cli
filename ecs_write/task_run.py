#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-tasks.html
	list-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-tasks.html
	start-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/start-task.html
	stop-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/stop-task.html
    """

    write_parameter("ecs", "run-task")