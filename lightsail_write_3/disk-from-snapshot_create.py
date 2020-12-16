#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk-from-snapshot.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # disk-name : The unique Lightsail disk name (e.g., my-disk ).
    # availability-zone : The Availability Zone where you want to create the disk (e.g., us-east-2a ). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.
Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.
    # size-in-gb : The size of the disk in GB (e.g., 32 ).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lightsail", "create-disk-from-snapshot", "disk-name", "availability-zone", "size-in-gb", add_option_dict)
