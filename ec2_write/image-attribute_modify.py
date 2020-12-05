#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-image-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-image-attribute.html
	reset-image-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-image-attribute.html
    """

    write_parameter("ec2", "modify-image-attribute")