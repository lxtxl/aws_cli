#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/put-backup-vault-notifications.html
if __name__ == '__main__':
    """
	delete-backup-vault-notifications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-backup-vault-notifications.html
	get-backup-vault-notifications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-vault-notifications.html
    """

    parameter_display_string = """
    # backup-vault-name : The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    # sns-topic-arn : The Amazon Resource Name (ARN) that specifies the topic for a backup vaultâs events; for example, arn:aws:sns:us-west-2:111122223333:MyVaultTopic .
    # backup-vault-events : An array of events that indicate the status of jobs to back up resources to the backup vault.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("backup", "put-backup-vault-notifications", "backup-vault-name", "sns-topic-arn", "backup-vault-events", add_option_dict)
