#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-code-signing-config.html
if __name__ == '__main__':
    """
	get-function-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-code-signing-config.html
	put-function-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-code-signing-config.html
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
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lambda", "delete-function-code-signing-config", "function-name", add_option_dict)





