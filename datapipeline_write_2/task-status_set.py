#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/set-task-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # task-id : The ID of the task assigned to the task runner. This value is provided in the response for  PollForTask .
    # task-status : If FINISHED , the task successfully completed. If FAILED , the task ended unsuccessfully. Preconditions use false.
Possible values:

FINISHED
FAILED
FALSE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("datapipeline", "set-task-status", "task-id", "task-status", add_option_dict)
