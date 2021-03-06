#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-set.html
	describe-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set.html
	list-stack-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-sets.html
	update-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-set.html
    """

    write_parameter("cloudformation", "create-stack-set")