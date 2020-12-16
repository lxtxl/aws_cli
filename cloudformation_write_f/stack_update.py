#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack.html
	delete-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack.html
	describe-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stacks.html
	list-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stacks.html
    """

    write_parameter("cloudformation", "update-stack")