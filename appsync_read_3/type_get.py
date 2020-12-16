#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-type.html
if __name__ == '__main__':
    """
	create-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-type.html
	delete-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-type.html
	list-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-types.html
	update-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-type.html
    """

    parameter_display_string = """
    # api-id : The API ID.
    # type-name : The type name.
    """

    execute_two_parameter("appsync", "get-type", "api-id", "type-name", parameter_display_string)