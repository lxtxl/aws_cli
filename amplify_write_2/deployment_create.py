#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-deployment.html
if __name__ == '__main__':
    """
	start-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/start-deployment.html
    """

    parameter_display_string = """
    # app-id : The unique ID for an Amplify app.
    # branch-name : The name for the branch, for the job.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("amplify", "create-deployment", "app-id", "branch-name", add_option_dict)
