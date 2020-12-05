#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-project.html
if __name__ == '__main__':
    """
	create-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-project.html
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/delete-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-projects.html
    """

    parameter_display_string = """
    # role-arn : The Amazon Resource Name (ARN) of the IAM role to be assumed for this request.
    # name : The name of the project to be updated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("databrew", "update-project", "role-arn", "name", add_option_dict)
