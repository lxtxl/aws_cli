#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-workteam.html
if __name__ == '__main__':
    """
	create-workteam : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-workteam.html
	describe-workteam : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-workteam.html
	list-workteams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workteams.html
	update-workteam : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-workteam.html
    """

    parameter_display_string = """
    # workteam-name : The name of the work team to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "delete-workteam", "workteam-name", add_option_dict)





