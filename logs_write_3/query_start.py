#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-query.html
if __name__ == '__main__':
    """
	describe-queries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-queries.html
	stop-query : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/stop-query.html
    """

    parameter_display_string = """
    # start-time : 
    # end-time : 
    # query-string : The query string to use. For more information, see CloudWatch Logs Insights Query Syntax .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("logs", "start-query", "start-time", "end-time", "query-string", add_option_dict)
