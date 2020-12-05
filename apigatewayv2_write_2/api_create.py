#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-api.html
if __name__ == '__main__':
    """
	delete-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-api.html
	export-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/export-api.html
	get-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api.html
	get-apis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-apis.html
	import-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/import-api.html
	reimport-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/reimport-api.html
	update-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api.html
    """

    parameter_display_string = """
    # name : The name of the API.
    # protocol-type : The API protocol.
Possible values:

WEBSOCKET
HTTP
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigatewayv2", "create-api", "name", "protocol-type", add_option_dict)
