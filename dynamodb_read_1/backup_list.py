#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-backup.html
if __name__ == '__main__':
    """
	create-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-backup.html
	delete-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-backup.html
	list-backups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-backups.html
    """

    parameter_display_string = """
    # backup-arn : The Amazon Resource Name (ARN) associated with the backup.
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

    execute_one_parameter("dynamodb", "describe-backup", "backup-arn", add_option_dict)