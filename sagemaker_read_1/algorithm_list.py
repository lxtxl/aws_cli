#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-algorithm.html
if __name__ == '__main__':
    """
	create-algorithm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-algorithm.html
	delete-algorithm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-algorithm.html
	list-algorithms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-algorithms.html
    """

    parameter_display_string = """
    # algorithm-name : The name of the algorithm to describe.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("sagemaker", "describe-algorithm", "algorithm-name", add_option_dict)