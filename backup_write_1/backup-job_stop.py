#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/stop-backup-job.html
if __name__ == '__main__':
    """
	describe-backup-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-backup-job.html
	list-backup-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-jobs.html
	start-backup-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-backup-job.html
    """

    parameter_display_string = """
    # backup-job-id : Uniquely identifies a request to AWS Backup to back up a resource.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("backup", "stop-backup-job", "backup-job-id", add_option_dict)





