#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-backup-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-backup-plan.html
	get-backup-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-plan.html
	list-backup-plans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-plans.html
	update-backup-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/update-backup-plan.html
    """

    write_parameter("backup", "create-backup-plan")