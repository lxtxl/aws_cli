#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-route-response.html
if __name__ == '__main__':
    """
	delete-route-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-route-response.html
	get-route-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-route-response.html
	get-route-responses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-route-responses.html
	update-route-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-route-response.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # route-id : The route ID.
    # route-response-key : The route response key.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("apigatewayv2", "create-route-response", "api-id", "route-id", "route-response-key", add_option_dict)
