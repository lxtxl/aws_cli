#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-context.html
if __name__ == '__main__':
    """
	create-context : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-context.html
	describe-context : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-context.html
	list-contexts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-contexts.html
	update-context : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-context.html
    """

    parameter_display_string = """
    # context-name : The name of the context to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "delete-context", "context-name", add_option_dict)





