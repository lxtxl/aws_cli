#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deregister-task-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deregister-task-definition.html
	describe-task-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-task-definition.html
	list-task-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-task-definitions.html
    """

    write_parameter("ecs", "register-task-definition")