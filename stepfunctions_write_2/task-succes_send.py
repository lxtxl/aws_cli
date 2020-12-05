#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/send-task-success.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # task-token : The token that represents this task. Task tokens are generated by Step Functions when tasks are assigned to a worker, or in the context object when a workflow enters a task state. See  GetActivityTaskOutput$taskToken .
    # task-output : The JSON output of the task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("stepfunctions", "send-task-success", "task-token", "task-output", add_option_dict)
