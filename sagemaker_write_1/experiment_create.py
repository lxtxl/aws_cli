#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-experiment.html
if __name__ == '__main__':
    """
	delete-experiment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-experiment.html
	describe-experiment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-experiment.html
	list-experiments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-experiments.html
	update-experiment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-experiment.html
    """

    parameter_display_string = """
    # experiment-name : The name of the experiment. The name must be unique in your AWS account and is not case-sensitive.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "create-experiment", "experiment-name", add_option_dict)





