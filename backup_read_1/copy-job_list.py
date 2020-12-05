#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-copy-job.html
if __name__ == '__main__':
    """
	list-copy-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-copy-jobs.html
	start-copy-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-copy-job.html
    """

    parameter_display_string = """
    # copy-job-id : Uniquely identifies a copy job.
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

    execute_one_parameter("backup", "describe-copy-job", "copy-job-id", add_option_dict)