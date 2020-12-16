#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-disk.html
if __name__ == '__main__':
    """
	create-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk.html
	delete-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-disk.html
	detach-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/detach-disk.html
	get-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk.html
	get-disks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disks.html
    """

    parameter_display_string = """
    # disk-name : The unique Lightsail disk name (e.g., my-disk ).
    # instance-name : The name of the Lightsail instance where you want to utilize the storage disk.
    # disk-path : The disk path to expose to the instance (e.g., /dev/xvdf ).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lightsail", "attach-disk", "disk-name", "instance-name", "disk-path", add_option_dict)
