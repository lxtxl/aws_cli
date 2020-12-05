#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-endpoint-weights-and-capacities.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # endpoint-name : The name of an existing Amazon SageMaker endpoint.
    # desired-weights-and-capacities : An object that provides new capacity and weight values for a variant.
(structure)

Specifies weight and capacity values for a production variant.
VariantName -> (string)

The name of the variant to update.

DesiredWeight -> (float)

The variantâs weight.

DesiredInstanceCount -> (integer)

The variantâs capacity.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "update-endpoint-weights-and-capacities", "endpoint-name", "desired-weights-and-capacities", add_option_dict)
