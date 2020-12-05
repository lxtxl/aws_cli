#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-authorizer.html
if __name__ == '__main__':
    """
	create-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-authorizer.html
	delete-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-authorizer.html
	get-authorizers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-authorizers.html
	update-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-authorizer.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # authorizer-id : The authorizer identifier.
    """

    execute_two_parameter("apigatewayv2", "get-authorizer", "api-id", "authorizer-id", parameter_display_string)