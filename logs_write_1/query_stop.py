#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/stop-query.html
if __name__ == '__main__':
    """
	describe-queries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-queries.html
	start-query : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-query.html
    """

    parameter_display_string = """
    # query-id : The ID number of the query to stop. To find this ID number, use DescribeQueries .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("logs", "stop-query", "query-id", add_option_dict)





