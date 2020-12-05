#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/update-dataset-group.html
if __name__ == '__main__':
    """
	create-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-dataset-group.html
	delete-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-dataset-group.html
	describe-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset-group.html
	list-dataset-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-dataset-groups.html
    """

    parameter_display_string = """
    # dataset-group-arn : The ARN of the dataset group.
    # dataset-arns : An array of the Amazon Resource Names (ARNs) of the datasets to add to the dataset group.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("forecast", "update-dataset-group", "dataset-group-arn", "dataset-arns", add_option_dict)
