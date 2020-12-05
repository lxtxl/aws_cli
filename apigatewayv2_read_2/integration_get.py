#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integration.html
if __name__ == '__main__':
    """
	create-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-integration.html
	delete-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-integration.html
	get-integrations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integrations.html
	update-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-integration.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # integration-id : The integration ID.
    """

    execute_two_parameter("apigatewayv2", "get-integration", "api-id", "integration-id", parameter_display_string)