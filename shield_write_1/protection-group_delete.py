#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/delete-protection-group.html
if __name__ == '__main__':
    """
	create-protection-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection-group.html
	describe-protection-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-protection-group.html
	list-protection-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-protection-groups.html
	update-protection-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/update-protection-group.html
    """

    parameter_display_string = """
    # protection-group-id : The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("shield", "delete-protection-group", "protection-group-id", add_option_dict)





