#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-backup-vault : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-vault.html
	describe-backup-vault : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-backup-vault.html
	list-backup-vaults : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-vaults.html
    """

    write_parameter("backup", "delete-backup-vault")