#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-route.html
if __name__ == '__main__':
    """
	delete-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-route.html
	get-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-route.html
	get-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-routes.html
	update-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-route.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # route-key : The route key for the route.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigatewayv2", "create-route", "api-id", "route-key", add_option_dict)
