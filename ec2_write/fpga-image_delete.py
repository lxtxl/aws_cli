#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	copy-fpga-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-fpga-image.html
	create-fpga-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fpga-image.html
	describe-fpga-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fpga-images.html
    """

    write_parameter("ec2", "delete-fpga-image")