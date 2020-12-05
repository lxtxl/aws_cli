#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-project.html
if __name__ == '__main__':
    """
	create-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/create-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-projects.html
	update-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-project.html
    """

    parameter_display_string = """
    # name : The name of the build project.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codebuild", "delete-project", "name", add_option_dict)





