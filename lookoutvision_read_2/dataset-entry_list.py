#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/list-dataset-entries.html
if __name__ == '__main__':
    """
	update-dataset-entries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/update-dataset-entries.html
    """

    parameter_display_string = """
    # project-name : The name of the project that contains the dataset that you want to list.
    # dataset-type : The type of the dataset that you want to list. Specify train to list the training dataset. Specify test to list the test dataset. If you have a single dataset project, specify train .
    """

    execute_two_parameter("lookoutvision", "list-dataset-entries", "project-name", "dataset-type", parameter_display_string)