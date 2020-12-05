#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/stop-thing-registration-task.html
if __name__ == '__main__':
    """
	describe-thing-registration-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-registration-task.html
	list-thing-registration-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-registration-tasks.html
	start-thing-registration-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/start-thing-registration-task.html
    """

    parameter_display_string = """
    # task-id : The bulk thing provisioning task ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "stop-thing-registration-task", "task-id", add_option_dict)





