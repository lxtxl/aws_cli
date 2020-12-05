#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-authorizer.html
if __name__ == '__main__':
    """
	create-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-authorizer.html
	delete-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-authorizer.html
	get-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-authorizer.html
	get-authorizers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-authorizers.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # authorizer-id : The authorizer identifier.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigatewayv2", "update-authorizer", "api-id", "authorizer-id", add_option_dict)
