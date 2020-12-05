#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/request-cancel-workflow-execution.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # domain : The name of the domain containing the workflow execution to cancel.
    # workflow-id : The workflowId of the workflow execution to cancel.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("swf", "request-cancel-workflow-execution", "domain", "workflow-id", add_option_dict)
