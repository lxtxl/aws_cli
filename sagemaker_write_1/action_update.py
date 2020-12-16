#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-action.html
if __name__ == '__main__':
    """
	create-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-action.html
	delete-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-action.html
	describe-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-action.html
	list-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-actions.html
    """

    parameter_display_string = """
    # action-name : The name of the action to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "update-action", "action-name", add_option_dict)





