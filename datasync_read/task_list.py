#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-tasks.html
if __name__ == '__main__':
    """
	create-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-task.html
	delete-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/delete-task.html
	describe-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-task.html
	update-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-task.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("datasync", "list-tasks", add_option_dict)