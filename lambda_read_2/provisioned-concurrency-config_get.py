#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-provisioned-concurrency-config.html
if __name__ == '__main__':
    """
	delete-provisioned-concurrency-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-provisioned-concurrency-config.html
	list-provisioned-concurrency-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-provisioned-concurrency-configs.html
	put-provisioned-concurrency-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-provisioned-concurrency-config.html
    """

    parameter_display_string = """
    # function-name : The name of the Lambda function.

Name formats


Function name - my-function .
Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .
Partial ARN - 123456789012:function:my-function .

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
    # qualifier : The version number or alias name.
    """

    execute_two_parameter("lambda", "get-provisioned-concurrency-config", "function-name", "qualifier", parameter_display_string)