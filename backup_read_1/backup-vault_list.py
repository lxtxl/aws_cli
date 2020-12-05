#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-backup-vault.html
if __name__ == '__main__':
    """
	create-backup-vault : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-vault.html
	delete-backup-vault : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-backup-vault.html
	list-backup-vaults : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-vaults.html
    """

    parameter_display_string = """
    # backup-vault-name : The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
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

    execute_one_parameter("backup", "describe-backup-vault", "backup-vault-name", add_option_dict)