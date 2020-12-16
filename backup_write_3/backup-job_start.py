#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-backup-job.html
if __name__ == '__main__':
    """
	describe-backup-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-backup-job.html
	list-backup-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-jobs.html
	stop-backup-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/stop-backup-job.html
    """

    parameter_display_string = """
    # backup-vault-name : The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    # resource-arn : An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
    # iam-role-arn : Specifies the IAM role ARN used to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("backup", "start-backup-job", "backup-vault-name", "resource-arn", "iam-role-arn", add_option_dict)
