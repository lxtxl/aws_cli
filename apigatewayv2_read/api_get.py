#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-apis.html
if __name__ == '__main__':
    """
	create-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-api.html
	delete-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-api.html
	export-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/export-api.html
	get-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api.html
	import-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/import-api.html
	reimport-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/reimport-api.html
	update-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("apigatewayv2", "get-apis", add_option_dict)