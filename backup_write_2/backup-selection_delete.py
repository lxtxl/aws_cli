#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-backup-selection.html
if __name__ == '__main__':
    """
	create-backup-selection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-selection.html
	get-backup-selection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-selection.html
	list-backup-selections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-selections.html
    """

    parameter_display_string = """
    # backup-plan-id : Uniquely identifies a backup plan.
    # selection-id : Uniquely identifies the body of a request to assign a set of resources to a backup plan.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("backup", "delete-backup-selection", "backup-plan-id", "selection-id", add_option_dict)
