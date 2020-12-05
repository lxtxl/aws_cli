#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-registration-task-reports.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # task-id : The id of the task.
    # report-type : The type of task report.
Possible values:

ERRORS
RESULTS
    """

    execute_two_parameter("iot", "list-thing-registration-task-reports", "task-id", "report-type", parameter_display_string)