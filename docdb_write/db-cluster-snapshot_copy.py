#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-cluster-snapshot.html
	delete-db-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-cluster-snapshot.html
	describe-db-cluster-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-snapshots.html
    """

    write_parameter("docdb", "copy-db-cluster-snapshot")