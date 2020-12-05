#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-introspection-schema.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # api-id : The API ID.
    # format : The schema format: SDL or JSON.
Possible values:

SDL
JSON
    """

    execute_two_parameter("appsync", "get-introspection-schema", "api-id", "format", parameter_display_string)