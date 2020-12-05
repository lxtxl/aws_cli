#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-function.html
if __name__ == '__main__':
    """
	create-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-function.html
	delete-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-function.html
	list-functions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-functions.html
	update-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-function.html
    """

    parameter_display_string = """
    # api-id : The GraphQL API ID.
    # function-id : The Function ID.
    """

    execute_two_parameter("appsync", "get-function", "api-id", "function-id", parameter_display_string)