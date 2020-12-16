#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-project.html
if __name__ == '__main__':
    """
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/delete-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/list-projects.html
    """

    parameter_display_string = """
    # project-name : S nsme for the project.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lookoutvision", "create-project", "project-name", add_option_dict)





