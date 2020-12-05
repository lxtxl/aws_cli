#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-branch.html
if __name__ == '__main__':
    """
	delete-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-branch.html
	get-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-branch.html
	list-branches : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-branches.html
	update-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/update-branch.html
    """

    parameter_display_string = """
    # app-id : The unique ID for an Amplify app.
    # branch-name : The name for the branch.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("amplify", "create-branch", "app-id", "branch-name", add_option_dict)
