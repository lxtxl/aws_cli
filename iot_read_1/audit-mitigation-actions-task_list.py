#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-mitigation-actions-task.html
if __name__ == '__main__':
    """
	cancel-audit-mitigation-actions-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-audit-mitigation-actions-task.html
	list-audit-mitigation-actions-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-mitigation-actions-tasks.html
	start-audit-mitigation-actions-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/start-audit-mitigation-actions-task.html
    """

    parameter_display_string = """
    # task-id : The unique identifier for the audit mitigation task.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("iot", "describe-audit-mitigation-actions-task", "task-id", add_option_dict)