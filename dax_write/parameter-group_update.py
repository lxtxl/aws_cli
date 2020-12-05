#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/create-parameter-group.html
	delete-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-parameter-group.html
	describe-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-parameter-groups.html
    """

    write_parameter("dax", "update-parameter-group")