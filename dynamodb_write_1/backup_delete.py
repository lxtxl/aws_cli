#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-backup.html
if __name__ == '__main__':
    """
	create-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-backup.html
	describe-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-backup.html
	list-backups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-backups.html
    """

    parameter_display_string = """
    # backup-arn : The ARN associated with the backup.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dynamodb", "delete-backup", "backup-arn", add_option_dict)





