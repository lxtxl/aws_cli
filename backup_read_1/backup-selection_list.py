#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-selections.html
if __name__ == '__main__':
    """
	create-backup-selection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-selection.html
	delete-backup-selection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-backup-selection.html
	get-backup-selection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-selection.html
    """

    parameter_display_string = """
    # backup-plan-id : Uniquely identifies a backup plan.
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

    execute_one_parameter("backup", "list-backup-selections", "backup-plan-id", add_option_dict)