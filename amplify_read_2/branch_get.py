#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-branch.html
if __name__ == '__main__':
    """
	create-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-branch.html
	delete-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-branch.html
	list-branches : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-branches.html
	update-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/update-branch.html
    """

    parameter_display_string = """
    # app-id : The unique ID for an Amplify app.
    # branch-name : The name for the branch.
    """

    execute_two_parameter("amplify", "get-branch", "app-id", "branch-name", parameter_display_string)