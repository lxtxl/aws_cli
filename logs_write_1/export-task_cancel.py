#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/cancel-export-task.html
if __name__ == '__main__':
    """
	create-export-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-export-task.html
	describe-export-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-export-tasks.html
    """

    parameter_display_string = """
    # task-id : The ID of the export task.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("logs", "cancel-export-task", "task-id", add_option_dict)





