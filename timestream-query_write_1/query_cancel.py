#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/cancel-query.html
if __name__ == '__main__':
    """
	query : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/query.html
    """

    parameter_display_string = """
    # query-id : The id of the query that needs to be cancelled. QueryID is returned as part of QueryResult.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("timestream-query", "cancel-query", "query-id", add_option_dict)





