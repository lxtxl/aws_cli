#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-graphql-api.html
if __name__ == '__main__':
    """
	create-graphql-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-graphql-api.html
	delete-graphql-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-graphql-api.html
	list-graphql-apis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-graphql-apis.html
	update-graphql-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-graphql-api.html
    """

    parameter_display_string = """
    # api-id : The API ID for the GraphQL API.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("appsync", "get-graphql-api", "api-id", add_option_dict)