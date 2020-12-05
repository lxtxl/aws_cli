#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-instance-snapshot.html
if __name__ == '__main__':
    """
	create-instance-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instance-snapshot.html
	get-instance-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-snapshot.html
	get-instance-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-snapshots.html
    """

    parameter_display_string = """
    # instance-snapshot-name : The name of the snapshot to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "delete-instance-snapshot", "instance-snapshot-name", add_option_dict)





