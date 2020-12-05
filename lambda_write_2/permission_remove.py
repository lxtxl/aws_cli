#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-permission.html
if __name__ == '__main__':
    """
	add-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html
    """

    parameter_display_string = """
    # function-name : The name of the Lambda function, version, or alias.

Name formats


Function name - my-function (name-only), my-function:v1 (with alias).
Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .
Partial ARN - 123456789012:function:my-function .

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
    # statement-id : Statement ID of the permission to remove.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lambda", "remove-permission", "function-name", "statement-id", add_option_dict)
