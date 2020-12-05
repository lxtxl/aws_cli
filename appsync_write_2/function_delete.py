#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-function.html
if __name__ == '__main__':
    """
	create-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-function.html
	get-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-function.html
	list-functions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-functions.html
	update-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-function.html
    """

    parameter_display_string = """
    # api-id : The GraphQL API ID.
    # function-id : The Function ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appsync", "delete-function", "api-id", "function-id", add_option_dict)
