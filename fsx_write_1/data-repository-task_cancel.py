#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/cancel-data-repository-task.html
if __name__ == '__main__':
    """
	create-data-repository-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-data-repository-task.html
	describe-data-repository-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-data-repository-tasks.html
    """

    parameter_display_string = """
    # task-id : Specifies the data repository task to cancel.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("fsx", "cancel-data-repository-task", "task-id", add_option_dict)





