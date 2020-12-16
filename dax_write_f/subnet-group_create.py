#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-subnet-group.html
	describe-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-subnet-groups.html
	update-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/update-subnet-group.html
    """

    write_parameter("dax", "create-subnet-group")