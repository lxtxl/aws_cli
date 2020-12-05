#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/delete-task.html
if __name__ == '__main__':
    """
	create-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-task.html
	describe-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-task.html
	list-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-tasks.html
	update-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-task.html
    """

    parameter_display_string = """
    # task-arn : The Amazon Resource Name (ARN) of the task to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("datasync", "delete-task", "task-arn", add_option_dict)





