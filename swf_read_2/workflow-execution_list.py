#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-execution.html
if __name__ == '__main__':
    """
	signal-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/signal-workflow-execution.html
	start-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/start-workflow-execution.html
	terminate-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/terminate-workflow-execution.html
    """

    parameter_display_string = """
    # domain : The name of the domain containing the workflow execution.
    # execution : 
    """

    execute_two_parameter("swf", "describe-workflow-execution", "domain", "execution", parameter_display_string)