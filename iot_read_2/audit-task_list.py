#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-tasks.html
if __name__ == '__main__':
    """
	cancel-audit-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-audit-task.html
	describe-audit-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-task.html
    """

    parameter_display_string = """
    # start-time : 
    # end-time : 
    """

    execute_two_parameter("iot", "list-audit-tasks", "start-time", "end-time", parameter_display_string)