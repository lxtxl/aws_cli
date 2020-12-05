#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-authorizer.html
if __name__ == '__main__':
    """
	delete-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-authorizer.html
	describe-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-authorizer.html
	list-authorizers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-authorizers.html
	update-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-authorizer.html
    """

    parameter_display_string = """
    # authorizer-name : The authorizer name.
    # authorizer-function-arn : The ARN of the authorizerâs Lambda function.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "create-authorizer", "authorizer-name", "authorizer-function-arn", add_option_dict)
