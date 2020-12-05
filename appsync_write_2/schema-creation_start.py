#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/start-schema-creation.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # api-id : The API ID.
    # definition : The type definition, in GraphQL Schema Definition Language (SDL) format.
For more information, see the GraphQL SDL documentation .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appsync", "start-schema-creation", "api-id", "definition", add_option_dict)
