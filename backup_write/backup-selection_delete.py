#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-backup-selection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-selection.html
	get-backup-selection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-selection.html
	list-backup-selections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-selections.html
    """

    write_parameter("backup", "delete-backup-selection")