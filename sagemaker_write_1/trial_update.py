#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-trial.html
if __name__ == '__main__':
    """
	create-trial : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-trial.html
	delete-trial : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-trial.html
	describe-trial : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-trial.html
	list-trials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-trials.html
    """

    parameter_display_string = """
    # trial-name : The name of the trial to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "update-trial", "trial-name", add_option_dict)





