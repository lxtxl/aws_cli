#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-lifecycle-hook : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-lifecycle-hook.html
	describe-lifecycle-hooks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-lifecycle-hooks.html
    """

    write_parameter("autoscaling", "put-lifecycle-hook")