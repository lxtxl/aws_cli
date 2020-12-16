#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-artifact.html
if __name__ == '__main__':
    """
	delete-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-artifact.html
	describe-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-artifact.html
	list-artifacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-artifacts.html
	update-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-artifact.html
    """

    parameter_display_string = """
    # source : The parameter types to return. Specify user to show parameters that are different form the default. Similarly, specify engine-default to show parameters that are the same as the default parameter group.
Default: All parameter types returned.
Valid Values: user | engine-default
    # artifact-type : The artifact type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-artifact", "source", "artifact-type", add_option_dict)
