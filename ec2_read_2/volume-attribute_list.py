#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-attribute.html
if __name__ == '__main__':
    """
	modify-volume-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-volume-attribute.html
    """

    parameter_display_string = """
    # attribute : The attribute of the volume. This parameter is required.
Possible values:

autoEnableIO
productCodes
    # volume-id : The ID of the volume.
    """

    execute_two_parameter("ec2", "describe-volume-attribute", "attribute", "volume-id", parameter_display_string)