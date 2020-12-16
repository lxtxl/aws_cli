#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/delete-user-hierarchy-group.html
if __name__ == '__main__':
    """
	create-user-hierarchy-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-user-hierarchy-group.html
	describe-user-hierarchy-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user-hierarchy-group.html
	list-user-hierarchy-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-user-hierarchy-groups.html
    """

    parameter_display_string = """
    # hierarchy-group-id : The identifier of the hierarchy group.
    # instance-id : The identifier of the Amazon Connect instance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connect", "delete-user-hierarchy-group", "hierarchy-group-id", "instance-id", add_option_dict)
