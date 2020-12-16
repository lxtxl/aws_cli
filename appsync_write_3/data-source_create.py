#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-data-source.html
if __name__ == '__main__':
    """
	delete-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-data-source.html
	get-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-data-source.html
	list-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-data-sources.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-data-source.html
    """

    parameter_display_string = """
    # api-id : The API ID for the GraphQL API for the DataSource .
    # name : A user-supplied name for the DataSource .
    # type : The type of the DataSource .
Possible values:

AWS_LAMBDA
AMAZON_DYNAMODB
AMAZON_ELASTICSEARCH
NONE
HTTP
RELATIONAL_DATABASE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appsync", "create-data-source", "api-id", "name", "type", add_option_dict)
