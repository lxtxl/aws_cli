#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/cancel-export-task.html
if __name__ == '__main__':
    """
	describe-export-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-export-tasks.html
	start-export-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-export-task.html
    """

    parameter_display_string = """
    # export-task-identifier : The identifier of the snapshot export task to cancel.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "cancel-export-task", "export-task-identifier", add_option_dict)





