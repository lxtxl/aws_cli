#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-stack-set-operation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set-operation.html
	list-stack-set-operations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-set-operations.html
    """

    write_parameter("cloudformation", "stop-stack-set-operation")