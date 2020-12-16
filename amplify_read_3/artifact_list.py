#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-artifacts.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # app-id : The unique ID for an Amplify app.
    # branch-name : The name of a branch that is part of an Amplify app.
    """

    execute_two_parameter("amplify", "list-artifacts", "app-id", "branch-name", parameter_display_string)