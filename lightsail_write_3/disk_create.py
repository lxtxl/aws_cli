#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk.html
if __name__ == '__main__':
    """
	attach-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-disk.html
	delete-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-disk.html
	detach-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/detach-disk.html
	get-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk.html
	get-disks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disks.html
    """

    parameter_display_string = """
    # disk-name : The unique Lightsail disk name (e.g., my-disk ).
    # availability-zone : The Availability Zone where you want to create the disk (e.g., us-east-2a ). Use the same Availability Zone as the Lightsail instance to which you want to attach the disk.
Use the get regions operation to list the Availability Zones where Lightsail is currently available.
    # size-in-gb : The size of the disk in GB (e.g., 32 ).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lightsail", "create-disk", "disk-name", "availability-zone", "size-in-gb", add_option_dict)
