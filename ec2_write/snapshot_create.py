#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	copy-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-snapshot.html
	create-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-snapshots.html
	delete-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-snapshot.html
	describe-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshots.html
	import-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-snapshot.html
    """

    write_parameter("ec2", "create-snapshot")