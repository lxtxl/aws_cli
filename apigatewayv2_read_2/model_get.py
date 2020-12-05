#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-model.html
if __name__ == '__main__':
    """
	create-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-model.html
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-model.html
	get-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-models.html
	update-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-model.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # model-id : The model ID.
    """

    execute_two_parameter("apigatewayv2", "get-model", "api-id", "model-id", parameter_display_string)