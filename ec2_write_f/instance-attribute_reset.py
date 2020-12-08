#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-attribute.html
	modify-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-attribute.html
    """

    write_parameter("ec2", "reset-instance-attribute")