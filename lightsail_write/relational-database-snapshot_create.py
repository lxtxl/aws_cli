#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-relational-database-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-relational-database-snapshot.html
	get-relational-database-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshot.html
	get-relational-database-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshots.html
    """

    write_parameter("lightsail", "create-relational-database-snapshot")