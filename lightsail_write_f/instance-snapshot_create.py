#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-instance-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-instance-snapshot.html
	get-instance-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-snapshot.html
	get-instance-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-snapshots.html
    """

    write_parameter("lightsail", "create-instance-snapshot")