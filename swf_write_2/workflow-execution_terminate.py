#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/terminate-workflow-execution.html
if __name__ == '__main__':
    """
	describe-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-execution.html
	signal-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/signal-workflow-execution.html
	start-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/start-workflow-execution.html
    """

    parameter_display_string = """
    # domain : The domain of the workflow execution to terminate.
    # workflow-id : The workflowId of the workflow execution to terminate.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("swf", "terminate-workflow-execution", "domain", "workflow-id", add_option_dict)
