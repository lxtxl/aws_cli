#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-trial.html
if __name__ == '__main__':
    """
	delete-trial : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-trial.html
	describe-trial : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-trial.html
	list-trials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-trials.html
	update-trial : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-trial.html
    """

    parameter_display_string = """
    # trial-name : The name of the trial. The name must be unique in your AWS account and is not case-sensitive.
    # experiment-name : The name of the experiment to associate the trial with.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-trial", "trial-name", "experiment-name", add_option_dict)
