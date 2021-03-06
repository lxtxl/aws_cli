#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-change-set.html
	describe-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-change-set.html
	execute-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/execute-change-set.html
	list-change-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-change-sets.html
    """

    write_parameter("cloudformation", "delete-change-set")