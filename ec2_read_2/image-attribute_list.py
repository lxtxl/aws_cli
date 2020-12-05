#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-image-attribute.html
if __name__ == '__main__':
    """
	modify-image-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-image-attribute.html
	reset-image-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-image-attribute.html
    """

    parameter_display_string = """
    # attribute : The AMI attribute.

Note : Depending on your account privileges, the blockDeviceMapping attribute may return a Client.AuthFailure error. If this happens, use  DescribeImages to get information about the block device mapping for the AMI.

Possible values:

description
kernel
ramdisk
launchPermission
productCodes
blockDeviceMapping
sriovNetSupport
    # image-id : The ID of the AMI.
    """

    execute_two_parameter("ec2", "describe-image-attribute", "attribute", "image-id", parameter_display_string)