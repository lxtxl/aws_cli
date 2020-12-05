#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-enable-standards.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # standards-subscription-requests : The list of standards checks to enable.
(structure)

The standard that you want to enable.
StandardsArn -> (string)

The ARN of the standard that you want to enable. To view the list of available standards and their ARNs, use the ``  DescribeStandards `` operation.

StandardsInput -> (map)

A key-value pair of input for the standard.
key -> (string)
value -> (string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("securityhub", "batch-enable-standards", "standards-subscription-requests", add_option_dict)





