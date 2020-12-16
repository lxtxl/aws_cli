#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-type.html
	list-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-types.html
	register-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/register-type.html
    """

    write_parameter("cloudformation", "deregister-type")