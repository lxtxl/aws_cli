#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-layer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-layer.html
	describe-layers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-layers.html
	update-layer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-layer.html
    """

    write_parameter("opsworks", "delete-layer")