#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deploy.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # template-file : The path where your AWS CloudFormation template is located.
    # stack-name : The name of the AWS CloudFormation stack youâre deploying to. If you specify an existing stack, the command updates the stack. If you specify a new stack, the command creates it.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudformation", "deploy", "template-file", "stack-name", add_option_dict)
