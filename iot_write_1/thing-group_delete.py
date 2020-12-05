#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing-group.html
if __name__ == '__main__':
    """
	create-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-group.html
	describe-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-group.html
	list-thing-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-groups.html
	update-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing-group.html
    """

    parameter_display_string = """
    # thing-group-name : The name of the thing group to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "delete-thing-group", "thing-group-name", add_option_dict)





