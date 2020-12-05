#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-data-source.html
if __name__ == '__main__':
    """
	create-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-data-source.html
	delete-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-data-source.html
	list-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-data-sources.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-data-source.html
    """

    parameter_display_string = """
    # api-id : The API ID.
    # name : The name of the data source.
    """

    execute_two_parameter("appsync", "get-data-source", "api-id", "name", parameter_display_string)