#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-context.html
if __name__ == '__main__':
    """
	delete-context : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-context.html
	describe-context : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-context.html
	list-contexts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-contexts.html
	update-context : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-context.html
    """

    parameter_display_string = """
    # context-name : The name of the context. Must be unique to your account in an AWS Region.
    # source : The parameter types to return. Specify user to show parameters that are different form the default. Similarly, specify engine-default to show parameters that are the same as the default parameter group.
Default: All parameter types returned.
Valid Values: user | engine-default
    # context-type : The context type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sagemaker", "create-context", "context-name", "source", "context-type", add_option_dict)
