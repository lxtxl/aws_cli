#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-run.html
if __name__ == '__main__':
    """
	cancel-ml-task-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/cancel-ml-task-run.html
	get-ml-task-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-runs.html
    """

    parameter_display_string = """
    # transform-id : The unique identifier of the machine learning transform.
    # task-run-id : The unique identifier of the task run.
    """

    execute_two_parameter("glue", "get-ml-task-run", "transform-id", "task-run-id", parameter_display_string)