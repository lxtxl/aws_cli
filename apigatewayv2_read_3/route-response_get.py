#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-route-response.html
if __name__ == '__main__':
    """
	create-route-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-route-response.html
	delete-route-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-route-response.html
	get-route-responses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-route-responses.html
	update-route-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-route-response.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # route-id : The route ID.
    """

    execute_two_parameter("apigatewayv2", "get-route-response", "api-id", "route-id", parameter_display_string)