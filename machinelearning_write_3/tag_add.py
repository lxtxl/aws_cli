#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/add-tags.html
if __name__ == '__main__':
    """
	delete-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-tags.html
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-tags.html
    """

    parameter_display_string = """
    # tags : The key-value pairs to use to create tags. If you specify a key without specifying a value, Amazon ML creates a tag with the specified key and a value of null.
(structure)

A custom key-value pair associated with an ML object, such as an ML model.
Key -> (string)

A unique identifier for the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.

Value -> (string)

An optional string, typically used to describe or define the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.
    # resource-id : The ID of the ML object to tag. For example, exampleModelId .
    # resource-type : The type of the ML object to tag.
Possible values:

BatchPrediction
DataSource
Evaluation
MLModel
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("machinelearning", "add-tags", "tags", "resource-id", "resource-type", add_option_dict)
