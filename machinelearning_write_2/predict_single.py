#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/predict.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # ml-model-id : A unique identifier of the MLModel .
    # record : A map of variable name-value pairs that represent an observation.
key -> (string)

The name of a variable. Currently itâs used to specify the name of the target value, label, weight, and tags.

value -> (string)

The value of a variable. Currently itâs used to specify values of the target value, weights, and tag variables and for filtering variable values.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("machinelearning", "predict", "ml-model-id", "record", add_option_dict)
