#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-api-key.html
if __name__ == '__main__':
    """
	create-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-api-key.html
	delete-api-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-api-key.html
	list-api-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-api-keys.html
    """

    parameter_display_string = """
    # api-id : The ID for the GraphQL API.
    # id : The API key ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appsync", "update-api-key", "api-id", "id", add_option_dict)
