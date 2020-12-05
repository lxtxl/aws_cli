#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/import-api-keys.html
if __name__ == '__main__':
    """
	create-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-api-key.html
	delete-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-api-key.html
	get-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-key.html
	get-api-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-keys.html
	update-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-api-key.html
    """

    parameter_display_string = """
    # body : 
    # format : A query parameter to specify the input format to imported API keys. Currently, only the csv format is supported.
Possible values:

csv
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "import-api-keys", "body", "format", add_option_dict)
