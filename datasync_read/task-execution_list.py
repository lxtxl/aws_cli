#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-task-executions.html
if __name__ == '__main__':
    """
	cancel-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/cancel-task-execution.html
	describe-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-task-execution.html
	start-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/start-task-execution.html
	update-task-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-task-execution.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("datasync", "list-task-executions", add_option_dict)