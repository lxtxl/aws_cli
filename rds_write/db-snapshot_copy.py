#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-snapshot.html
	delete-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-snapshot.html
	describe-db-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshots.html
	modify-db-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot.html
    """

    write_parameter("rds", "copy-db-snapshot")