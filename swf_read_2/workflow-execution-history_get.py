#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/get-workflow-execution-history.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # domain : The name of the domain containing the workflow execution.
    # execution : 
    """

    execute_two_parameter("swf", "get-workflow-execution-history", "domain", "execution", parameter_display_string)