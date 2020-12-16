#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-type.html
if __name__ == '__main__':
    """
	create-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html
	delete-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-type.html
	get-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-type.html
	list-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-types.html
    """

    parameter_display_string = """
    # api-id : The API ID.
    # type-name : The new type name.
    # format : The new type format: SDL or JSON.
Possible values:

SDL
JSON
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appsync", "update-type", "api-id", "type-name", "format", add_option_dict)
