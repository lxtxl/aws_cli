#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api-mapping.html
if __name__ == '__main__':
    """
	create-api-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-api-mapping.html
	delete-api-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-api-mapping.html
	get-api-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api-mappings.html
	update-api-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api-mapping.html
    """

    parameter_display_string = """
    # api-mapping-id : The API mapping identifier.
    # domain-name : The domain name.
    """

    execute_two_parameter("apigatewayv2", "get-api-mapping", "api-mapping-id", "domain-name", parameter_display_string)