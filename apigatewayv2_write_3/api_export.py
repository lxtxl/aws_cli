#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/export-api.html
if __name__ == '__main__':
    """
	create-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-api.html
	delete-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-api.html
	get-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api.html
	get-apis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-apis.html
	import-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/import-api.html
	reimport-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/reimport-api.html
	update-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # output-type : The output type of the exported definition file. Valid values are JSON and YAML.
Possible values:

YAML
JSON
    # specification : The version of the API specification to use. OAS30, for OpenAPI 3.0, is the only supported value.
Possible values:

OAS30
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("apigatewayv2", "export-api", "api-id", "output-type", "specification", add_option_dict)
