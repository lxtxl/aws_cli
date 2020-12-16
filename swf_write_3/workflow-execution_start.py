#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/start-workflow-execution.html
if __name__ == '__main__':
    """
	describe-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-execution.html
	signal-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/signal-workflow-execution.html
	terminate-workflow-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/terminate-workflow-execution.html
    """

    parameter_display_string = """
    # domain : The name of the domain in which the workflow execution is created.
    # workflow-id : The user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a restart of a previous execution. You cannot have two open workflow executions with the same workflowId at the same time within the same domain.
The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\u0000-\u001f | \u007f-\u009f ). Also, it must not be the literal string arn .
    # workflow-type : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("swf", "start-workflow-execution", "domain", "workflow-id", "workflow-type", add_option_dict)
