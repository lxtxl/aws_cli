#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/update-dataset-entries.html
if __name__ == '__main__':
    """
	list-dataset-entries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/list-dataset-entries.html
    """

    parameter_display_string = """
    # project-name : The name of the project that contains the dataset that you want to update.
    # dataset-type : The type of the dataset that you want to update. Specify train to update the training dataset. Specify test to update the test dataset. If you have a single dataset project, specify train .
    # changes : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lookoutvision", "update-dataset-entries", "project-name", "dataset-type", "changes", add_option_dict)
