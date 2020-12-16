#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-project.html
if __name__ == '__main__':
    """
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-projects.html
    """

    parameter_display_string = """
    # project-name : The name of the project.
    # service-catalog-provisioning-details : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-project", "project-name", "service-catalog-provisioning-details", add_option_dict)
