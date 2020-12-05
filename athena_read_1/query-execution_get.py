#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-execution.html
if __name__ == '__main__':
    """
	list-query-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-query-executions.html
	start-query-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-query-execution.html
	stop-query-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/stop-query-execution.html
    """

    parameter_display_string = """
    # query-execution-id : The unique ID of the query execution.
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

    execute_one_parameter("athena", "get-query-execution", "query-execution-id", add_option_dict)