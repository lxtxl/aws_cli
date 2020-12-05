#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/restore-backup.html
if __name__ == '__main__':
    """
	delete-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/delete-backup.html
	describe-backups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/describe-backups.html
    """

    parameter_display_string = """
    # backup-id : The ID of the backup to be restored. To find the ID of a backup, use the  DescribeBackups operation.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudhsmv2", "restore-backup", "backup-id", add_option_dict)





