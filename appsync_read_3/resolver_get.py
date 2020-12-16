#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-resolver.html
if __name__ == '__main__':
    """
	create-resolver : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-resolver.html
	delete-resolver : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-resolver.html
	list-resolvers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-resolvers.html
	update-resolver : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-resolver.html
    """

    parameter_display_string = """
    # api-id : The API ID.
    # type-name : The resolver type name.
    """

    execute_two_parameter("appsync", "get-resolver", "api-id", "type-name", parameter_display_string)