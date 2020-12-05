#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-time-based-auto-scaling : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-time-based-auto-scaling.html
    """

    write_parameter("opsworks", "set-time-based-auto-scaling")