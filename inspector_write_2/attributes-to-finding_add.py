#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/add-attributes-to-findings.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # finding-arns : The ARNs that specify the findings that you want to assign attributes to.
(string)
    # attributes : The array of attributes that you want to assign to specified findings.
(structure)

This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
key -> (string)

The attribute key.

value -> (string)

The value assigned to the attribute key.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("inspector", "add-attributes-to-findings", "finding-arns", "attributes", add_option_dict)
