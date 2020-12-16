#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-route-request-parameter.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # api-id : The API identifier.
    # request-parameter-key : The route request parameter key.
    # route-id : The route ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("apigatewayv2", "delete-route-request-parameter", "api-id", "request-parameter-key", "route-id", add_option_dict)
