#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-algorithm.html
if __name__ == '__main__':
    """
	create-algorithm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-algorithm.html
	describe-algorithm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-algorithm.html
	list-algorithms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-algorithms.html
    """

    parameter_display_string = """
    # algorithm-name : The name of the algorithm to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "delete-algorithm", "algorithm-name", add_option_dict)





