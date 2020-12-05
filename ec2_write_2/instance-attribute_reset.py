#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-instance-attribute.html
if __name__ == '__main__':
    """
	describe-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-attribute.html
	modify-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-attribute.html
    """

    parameter_display_string = """
    # attribute : The attribute to reset.

Warning
You can only reset the following attributes: kernel | ramdisk | sourceDestCheck . To change an instance attribute, use  ModifyInstanceAttribute .

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
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "reset-instance-attribute", "attribute", "instance-id", add_option_dict)
