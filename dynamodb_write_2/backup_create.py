#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-backup.html
if __name__ == '__main__':
    """
	delete-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-backup.html
	describe-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-backup.html
	list-backups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-backups.html
    """

    parameter_display_string = """
    # table-name : The name of the table.
    # backup-name : Specified name for the backup.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "create-backup", "table-name", "backup-name", add_option_dict)
