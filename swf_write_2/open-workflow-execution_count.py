#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-open-workflow-executions.html
if __name__ == '__main__':
    """
	list-open-workflow-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-open-workflow-executions.html
    """

    parameter_display_string = """
    # domain : The name of the domain containing the workflow executions to count.
    # start-time-filter : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("swf", "count-open-workflow-executions", "domain", "start-time-filter", add_option_dict)
