#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/cancel-quantum-task.html
if __name__ == '__main__':
    """
	create-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/create-quantum-task.html
	get-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/get-quantum-task.html
	search-quantum-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/search-quantum-tasks.html
    """

    parameter_display_string = """
    # quantum-task-arn : The ARN of the task to cancel.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("braket", "cancel-quantum-task", "quantum-task-arn", add_option_dict)





