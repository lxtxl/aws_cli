#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-algorithm.html
if __name__ == '__main__':
    """
	delete-algorithm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-algorithm.html
	describe-algorithm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-algorithm.html
	list-algorithms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-algorithms.html
    """

    parameter_display_string = """
    # algorithm-name : The name of the algorithm.
    # training-specification : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-algorithm", "algorithm-name", "training-specification", add_option_dict)
