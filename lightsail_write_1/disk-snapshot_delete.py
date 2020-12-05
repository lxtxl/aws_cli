#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-disk-snapshot.html
if __name__ == '__main__':
    """
	create-disk-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk-snapshot.html
	get-disk-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk-snapshot.html
	get-disk-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk-snapshots.html
    """

    parameter_display_string = """
    # disk-snapshot-name : The name of the disk snapshot you want to delete (e.g., my-disk-snapshot ).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "delete-disk-snapshot", "disk-snapshot-name", add_option_dict)





