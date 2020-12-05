#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instance-snapshot.html
if __name__ == '__main__':
    """
	delete-instance-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-instance-snapshot.html
	get-instance-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-snapshot.html
	get-instance-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-snapshots.html
    """

    parameter_display_string = """
    # instance-snapshot-name : The name for your new snapshot.
    # instance-name : The Lightsail instance on which to base your snapshot.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "create-instance-snapshot", "instance-snapshot-name", "instance-name", add_option_dict)
