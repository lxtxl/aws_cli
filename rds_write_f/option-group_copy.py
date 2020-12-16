#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-option-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-option-group.html
	delete-option-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-option-group.html
	describe-option-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-option-groups.html
    """

    write_parameter("rds", "copy-option-group")