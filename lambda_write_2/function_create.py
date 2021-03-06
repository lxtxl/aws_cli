#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html
if __name__ == '__main__':
    """
	delete-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function.html
	get-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function.html
	list-functions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-functions.html
    """

    parameter_display_string = """
    # function-name : The name of the Lambda function.

Name formats


Function name - my-function .
Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .
Partial ARN - 123456789012:function:my-function .

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
    # role : The Amazon Resource Name (ARN) of the functionâs execution role.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lambda", "create-function", "function-name", "role", add_option_dict)
