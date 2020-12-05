#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-tags.html
if __name__ == '__main__':
    """
	add-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/add-tags.html
	delete-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-tags.html
    """

    parameter_display_string = """
    # resource-id : The ID of the ML object. For example, exampleModelId .
    # resource-type : The type of the ML object.
Possible values:

BatchPrediction
DataSource
Evaluation
MLModel
    """

    execute_two_parameter("machinelearning", "describe-tags", "resource-id", "resource-type", parameter_display_string)