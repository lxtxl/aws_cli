#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/cancel-ml-task-run.html
if __name__ == '__main__':
    """
	get-ml-task-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-run.html
	get-ml-task-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-runs.html
    """

    parameter_display_string = """
    # transform-id : The unique identifier of the machine learning transform.
    # task-run-id : A unique identifier for the task run.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "cancel-ml-task-run", "transform-id", "task-run-id", add_option_dict)
