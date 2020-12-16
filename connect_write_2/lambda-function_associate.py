#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-lambda-function.html
if __name__ == '__main__':
    """
	disassociate-lambda-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-lambda-function.html
	list-lambda-functions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-lambda-functions.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # function-arn : The Amazon Resource Name (ARN) for the Lambda function being associated. Maximum number of characters allowed is 140.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connect", "associate-lambda-function", "instance-id", "function-arn", add_option_dict)
