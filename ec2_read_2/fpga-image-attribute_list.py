#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fpga-image-attribute.html
if __name__ == '__main__':
    """
	modify-fpga-image-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-fpga-image-attribute.html
	reset-fpga-image-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-fpga-image-attribute.html
    """

    parameter_display_string = """
    # fpga-image-id : The ID of the AFI.
    # attribute : The AFI attribute.
Possible values:

description
name
loadPermission
productCodes
    """

    execute_two_parameter("ec2", "describe-fpga-image-attribute", "fpga-image-id", "attribute", parameter_display_string)