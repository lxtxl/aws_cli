#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-deployment.html
if __name__ == '__main__':
    """
	create-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-deployment.html
	delete-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-deployment.html
	get-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-deployments.html
	update-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-deployment.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # deployment-id : The deployment ID.
    """

    execute_two_parameter("apigatewayv2", "get-deployment", "api-id", "deployment-id", parameter_display_string)