#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-solution.html
if __name__ == '__main__':
    """
	delete-solution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-solution.html
	describe-solution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-solution.html
	list-solutions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-solutions.html
    """

    parameter_display_string = """
    # name : The name for the solution.
    # dataset-group-arn : The Amazon Resource Name (ARN) of the dataset group that provides the training data.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("personalize", "create-solution", "name", "dataset-group-arn", add_option_dict)
