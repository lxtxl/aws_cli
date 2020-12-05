#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-backup-plan.html
if __name__ == '__main__':
    """
	create-backup-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-plan.html
	get-backup-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-plan.html
	list-backup-plans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-plans.html
	update-backup-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/update-backup-plan.html
    """

    parameter_display_string = """
    # backup-plan-id : Uniquely identifies a backup plan.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("backup", "delete-backup-plan", "backup-plan-id", add_option_dict)





