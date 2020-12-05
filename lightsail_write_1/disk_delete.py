#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-disk.html
if __name__ == '__main__':
    """
	attach-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-disk.html
	create-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk.html
	detach-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/detach-disk.html
	get-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk.html
	get-disks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disks.html
    """

    parameter_display_string = """
    # disk-name : The unique name of the disk you want to delete (e.g., my-disk ).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "delete-disk", "disk-name", add_option_dict)





