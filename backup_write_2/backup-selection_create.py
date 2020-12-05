#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-selection.html
if __name__ == '__main__':
    """
	delete-backup-selection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-backup-selection.html
	get-backup-selection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-selection.html
	list-backup-selections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-selections.html
    """

    parameter_display_string = """
    # backup-plan-id : Uniquely identifies the backup plan to be associated with the selection of resources.
    # backup-selection : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("backup", "create-backup-selection", "backup-plan-id", "backup-selection", add_option_dict)
