#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-human-task-ui.html
if __name__ == '__main__':
    """
	create-human-task-ui : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-human-task-ui.html
	describe-human-task-ui : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-human-task-ui.html
	list-human-task-uis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-human-task-uis.html
    """

    parameter_display_string = """
    # human-task-ui-name : The name of the human task user interface (work task template) you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "delete-human-task-ui", "human-task-ui-name", add_option_dict)





