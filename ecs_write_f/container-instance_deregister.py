#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-container-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-container-instances.html
	list-container-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-container-instances.html
	register-container-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-container-instance.html
    """

    write_parameter("ecs", "deregister-container-instance")