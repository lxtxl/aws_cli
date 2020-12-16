#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-code-signing-config.html
if __name__ == '__main__':
    """
	delete-function-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-code-signing-config.html
	get-function-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-code-signing-config.html
    """

    parameter_display_string = """
    # code-signing-config-arn : The The Amazon Resource Name (ARN) of the code signing configuration.
    # function-name : The name of the Lambda function.

Name formats


Function name - MyFunction .
Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
Partial ARN - 123456789012:function:MyFunction .

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lambda", "put-function-code-signing-config", "code-signing-config-arn", "function-name", add_option_dict)
