#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-graphql-api.html
if __name__ == '__main__':
    """
	create-graphql-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-graphql-api.html
	delete-graphql-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-graphql-api.html
	get-graphql-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-graphql-api.html
	list-graphql-apis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-graphql-apis.html
    """

    parameter_display_string = """
    # api-id : The API ID.
    # name : The new name for the GraphqlApi object.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appsync", "update-graphql-api", "api-id", "name", add_option_dict)
