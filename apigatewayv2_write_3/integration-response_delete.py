#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-integration-response.html
if __name__ == '__main__':
    """
	create-integration-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-integration-response.html
	get-integration-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integration-response.html
	get-integration-responses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integration-responses.html
	update-integration-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-integration-response.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # integration-id : The integration ID.
    # integration-response-id : The integration response ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("apigatewayv2", "delete-integration-response", "api-id", "integration-id", "integration-response-id", add_option_dict)
