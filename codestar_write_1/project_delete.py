#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/delete-project.html
if __name__ == '__main__':
    """
	create-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/create-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/describe-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-projects.html
	tag-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/tag-project.html
	untag-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/untag-project.html
	update-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/update-project.html
    """

    parameter_display_string = """
    # id : The ID of the project to be deleted in AWS CodeStar.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codestar", "delete-project", "id", add_option_dict)





