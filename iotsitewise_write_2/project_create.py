#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-project.html
if __name__ == '__main__':
    """
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-projects.html
	update-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-project.html
    """

    parameter_display_string = """
    # portal-id : The ID of the portal in which to create the project.
    # project-name : A friendly name for the project.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotsitewise", "create-project", "portal-id", "project-name", add_option_dict)
