#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-tags.html
if __name__ == '__main__':
    """
	add-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/add-tags.html
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-tags.html
    """

    parameter_display_string = """
    # tag-keys : One or more tags to delete.
(string)
    # resource-id : The ID of the tagged ML object. For example, exampleModelId .
    # resource-type : The type of the tagged ML object.
Possible values:

BatchPrediction
DataSource
Evaluation
MLModel
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("machinelearning", "delete-tags", "tag-keys", "resource-id", "resource-type", add_option_dict)
