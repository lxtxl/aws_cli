#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing-group.html
if __name__ == '__main__':
    """
	create-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-group.html
	delete-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing-group.html
	describe-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-group.html
	list-thing-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-groups.html
    """

    parameter_display_string = """
    # thing-group-name : The thing group to update.
    # thing-group-properties : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "update-thing-group", "thing-group-name", "thing-group-properties", add_option_dict)
