#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-open-workflow-executions.html
if __name__ == '__main__':
    """
	count-open-workflow-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-open-workflow-executions.html
    """

    parameter_display_string = """
    # domain : The name of the domain that contains the workflow executions to list.
    # start-time-filter : 
    """

    execute_two_parameter("swf", "list-open-workflow-executions", "domain", "start-time-filter", parameter_display_string)