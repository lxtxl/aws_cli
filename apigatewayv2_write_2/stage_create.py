#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-stage.html
if __name__ == '__main__':
    """
	delete-stage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-stage.html
	get-stage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-stage.html
	get-stages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-stages.html
	update-stage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-stage.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # stage-name : The name of the stage.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigatewayv2", "create-stage", "api-id", "stage-name", add_option_dict)
