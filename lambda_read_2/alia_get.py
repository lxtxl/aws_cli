#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-alias.html
if __name__ == '__main__':
    """
	create-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-alias.html
	delete-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-alias.html
	update-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-alias.html
    """

    parameter_display_string = """
    # function-name : The name of the Lambda function.

Name formats


Function name - MyFunction .
Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
Partial ARN - 123456789012:function:MyFunction .

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
    # name : The name of the alias.
    """

    execute_two_parameter("lambda", "get-alias", "function-name", "name", parameter_display_string)