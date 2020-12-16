#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-stack.html
	describe-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-stacks.html
	update-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-stack.html
    """

    write_parameter("appstream", "create-stack")