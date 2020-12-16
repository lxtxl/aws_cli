#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-action.html
if __name__ == '__main__':
    """
	delete-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-action.html
	describe-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-action.html
	list-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-actions.html
	update-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-action.html
    """

    parameter_display_string = """
    # action-name : The name of the action. Must be unique to your account in an AWS Region.
    # source : The parameter types to return. Specify user to show parameters that are different form the default. Similarly, specify engine-default to show parameters that are the same as the default parameter group.
Default: All parameter types returned.
Valid Values: user | engine-default
    # action-type : The action type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sagemaker", "create-action", "action-name", "source", "action-type", add_option_dict)
