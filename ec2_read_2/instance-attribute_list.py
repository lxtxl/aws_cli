#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-attribute.html
if __name__ == '__main__':
    """
	modify-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-attribute.html
	reset-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-instance-attribute.html
    """

    parameter_display_string = """
    # attribute : The instance attribute.
Note: The enaSupport attribute is not supported at this time.
Possible values:

instanceType
kernel
ramdisk
userData
disableApiTermination
instanceInitiatedShutdownBehavior
rootDeviceName
blockDeviceMapping
productCodes
sourceDestCheck
groupSet
ebsOptimized
sriovNetSupport
enaSupport
enclaveOptions
    # instance-id : The ID of the instance.
    """

    execute_two_parameter("ec2", "describe-instance-attribute", "attribute", "instance-id", parameter_display_string)