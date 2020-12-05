#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-work-group.html
if __name__ == '__main__':
    """
	create-work-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-work-group.html
	delete-work-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-work-group.html
	get-work-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-work-group.html
	list-work-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-work-groups.html
    """

    parameter_display_string = """
    # work-group : The specified workgroup that will be updated.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("athena", "update-work-group", "work-group", add_option_dict)





