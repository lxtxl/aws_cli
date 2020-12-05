#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/restore-table-from-backup.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # target-table-name : The name of the new table to which the backup must be restored.
    # backup-arn : The Amazon Resource Name (ARN) associated with the backup.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "restore-table-from-backup", "target-table-name", "backup-arn", add_option_dict)
