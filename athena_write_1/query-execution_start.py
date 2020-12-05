#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-query-execution.html
if __name__ == '__main__':
    """
	get-query-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-execution.html
	list-query-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-query-executions.html
	stop-query-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/stop-query-execution.html
    """

    parameter_display_string = """
    # query-string : The SQL query statements to be executed.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("athena", "start-query-execution", "query-string", add_option_dict)





