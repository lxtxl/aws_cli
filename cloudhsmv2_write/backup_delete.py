#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-backups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/describe-backups.html
	restore-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/restore-backup.html
    """

    write_parameter("cloudhsmv2", "delete-backup")