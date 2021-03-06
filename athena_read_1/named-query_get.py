#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-named-query.html
if __name__ == '__main__':
    """
	create-named-query : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-named-query.html
	delete-named-query : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-named-query.html
	list-named-queries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-named-queries.html
    """

    parameter_display_string = """
    # named-query-id : The unique ID of the query. Use  ListNamedQueries to get query IDs.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("athena", "get-named-query", "named-query-id", add_option_dict)