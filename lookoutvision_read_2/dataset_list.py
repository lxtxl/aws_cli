#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-dataset.html
if __name__ == '__main__':
    """
	create-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-dataset.html
	delete-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/delete-dataset.html
    """

    parameter_display_string = """
    # project-name : The name of the project that contains the dataset that you want to describe.
    # dataset-type : The type of the dataset to describe. Specify train to describe the training dataset. Specify test to describe the test dataset. If you have a single dataset project, specify train
    """

    execute_two_parameter("lookoutvision", "describe-dataset", "project-name", "dataset-type", parameter_display_string)