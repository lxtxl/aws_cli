#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-concurrency.html
if __name__ == '__main__':
    """
	delete-function-concurrency : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-concurrency.html
	get-function-concurrency : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-concurrency.html
    """

    parameter_display_string = """
    # function-name : The name of the Lambda function.

Name formats


Function name - my-function .
Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .
Partial ARN - 123456789012:function:my-function .

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
    # reserved-concurrent-executions : The number of simultaneous executions to reserve for the function.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lambda", "put-function-concurrency", "function-name", "reserved-concurrent-executions", add_option_dict)
