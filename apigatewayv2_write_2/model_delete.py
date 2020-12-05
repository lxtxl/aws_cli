#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-model.html
if __name__ == '__main__':
    """
	create-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-model.html
	get-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-model.html
	get-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-models.html
	update-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-model.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # model-id : The model ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigatewayv2", "delete-model", "api-id", "model-id", add_option_dict)
