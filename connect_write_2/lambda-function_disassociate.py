#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-lambda-function.html
if __name__ == '__main__':
    """
	associate-lambda-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-lambda-function.html
	list-lambda-functions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-lambda-functions.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance..
    # function-arn : The Amazon Resource Name (ARN) of the Lambda function being disassociated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connect", "disassociate-lambda-function", "instance-id", "function-arn", add_option_dict)
