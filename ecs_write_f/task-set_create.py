#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-task-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-task-set.html
	describe-task-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-task-sets.html
	update-task-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-task-set.html
    """

    write_parameter("ecs", "create-task-set")