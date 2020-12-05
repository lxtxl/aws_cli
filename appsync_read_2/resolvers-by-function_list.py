#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-resolvers-by-function.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # api-id : The API ID.
    # function-id : The Function ID.
    """

    execute_two_parameter("appsync", "list-resolvers-by-function", "api-id", "function-id", parameter_display_string)