#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-auto-snapshot.html
if __name__ == '__main__':
    """
	get-auto-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-auto-snapshots.html
    """

    parameter_display_string = """
    # resource-name : The name of the source instance or disk from which to delete the automatic snapshot.
    # date : The date of the automatic snapshot to delete in YYYY-MM-DD format. Use the get auto snapshots operation to get the available automatic snapshots for a resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "delete-auto-snapshot", "resource-name", "date", add_option_dict)
