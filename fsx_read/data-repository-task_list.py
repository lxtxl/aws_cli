#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-data-repository-tasks.html
if __name__ == '__main__':
    """
	cancel-data-repository-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/cancel-data-repository-task.html
	create-data-repository-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-data-repository-task.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("fsx", "describe-data-repository-tasks", add_option_dict)