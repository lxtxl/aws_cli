#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-project.html
if __name__ == '__main__':
    """
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-project.html
	describe-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-projects.html
    """

    parameter_display_string = """
    # project-name : The name of the project to create.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rekognition", "create-project", "project-name", add_option_dict)





