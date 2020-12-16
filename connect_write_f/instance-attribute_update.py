#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-instance-attribute.html
	list-instance-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-instance-attributes.html
    """

    write_parameter("connect", "update-instance-attribute")