#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-api-mapping.html
if __name__ == '__main__':
    """
	delete-api-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-api-mapping.html
	get-api-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api-mapping.html
	get-api-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api-mappings.html
	update-api-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api-mapping.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # domain-name : The domain name.
    # stage : The API stage.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("apigatewayv2", "create-api-mapping", "api-id", "domain-name", "stage", add_option_dict)
