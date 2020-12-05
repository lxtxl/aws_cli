#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-api-cache.html
if __name__ == '__main__':
    """
	create-api-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-api-cache.html
	flush-api-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/flush-api-cache.html
	get-api-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-api-cache.html
	update-api-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-api-cache.html
    """

    parameter_display_string = """
    # api-id : The API ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appsync", "delete-api-cache", "api-id", add_option_dict)





