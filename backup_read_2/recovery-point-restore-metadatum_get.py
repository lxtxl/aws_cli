#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-recovery-point-restore-metadata.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # backup-vault-name : The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    # recovery-point-arn : An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .
    """

    execute_two_parameter("backup", "get-recovery-point-restore-metadata", "backup-vault-name", "recovery-point-arn", parameter_display_string)