#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-resolver.html
if __name__ == '__main__':
    """
	create-resolver : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-resolver.html
	get-resolver : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-resolver.html
	list-resolvers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-resolvers.html
	update-resolver : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-resolver.html
    """

    parameter_display_string = """
    # api-id : The API ID.
    # type-name : The name of the resolver type.
    # field-name : The resolver field name.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appsync", "delete-resolver", "api-id", "type-name", "field-name", add_option_dict)
