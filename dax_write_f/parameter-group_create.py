#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-parameter-group.html
	describe-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-parameter-groups.html
	update-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/update-parameter-group.html
    """

    write_parameter("dax", "create-parameter-group")