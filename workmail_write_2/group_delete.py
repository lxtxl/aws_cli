#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-group.html
if __name__ == '__main__':
    """
	create-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-group.html
	describe-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-groups.html
    """

    parameter_display_string = """
    # organization-id : The organization that contains the group.
    # group-id : The identifier of the group to be deleted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workmail", "delete-group", "organization-id", "group-id", add_option_dict)
