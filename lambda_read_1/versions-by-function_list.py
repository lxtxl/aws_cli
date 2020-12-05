#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-versions-by-function.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # function-name : The name of the Lambda function.

Name formats


Function name - MyFunction .
Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
Partial ARN - 123456789012:function:MyFunction .

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("lambda", "list-versions-by-function", "function-name", add_option_dict)