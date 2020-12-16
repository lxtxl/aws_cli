#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-dataset.html
if __name__ == '__main__':
    """
	delete-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/delete-dataset.html
	describe-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-dataset.html
    """

    parameter_display_string = """
    # project-name : The name of the project in which you want to create a dataset.
    # dataset-type : The type of the dataset. Specify train for a training dataset. Specify test for a test dataset.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lookoutvision", "create-dataset", "project-name", "dataset-type", add_option_dict)
