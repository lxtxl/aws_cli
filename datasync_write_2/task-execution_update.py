#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-task-execution.html
if __name__ == '__main__':
    """
	cancel-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/cancel-task-execution.html
	describe-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-task-execution.html
	list-task-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-task-executions.html
	start-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/start-task-execution.html
    """

    parameter_display_string = """
    # task-execution-arn : The Amazon Resource Name (ARN) of the specific task execution that is being updated.
    # options : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("datasync", "update-task-execution", "task-execution-arn", "options", add_option_dict)
