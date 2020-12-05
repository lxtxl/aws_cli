#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-backup-job.html
if __name__ == '__main__':
    """
	list-backup-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-jobs.html
	start-backup-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-backup-job.html
	stop-backup-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/stop-backup-job.html
    """

    parameter_display_string = """
    # backup-job-id : Uniquely identifies a request to AWS Backup to back up a resource.
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

    execute_one_parameter("backup", "describe-backup-job", "backup-job-id", add_option_dict)