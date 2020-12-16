#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-replication-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-instance.html
	delete-replication-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-instance.html
	describe-replication-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-instances.html
	modify-replication-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-instance.html
    """

    write_parameter("dms", "reboot-replication-instance")