#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-instance-storage-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-instance-storage-config.html
	disassociate-instance-storage-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-instance-storage-config.html
	list-instance-storage-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-instance-storage-configs.html
	update-instance-storage-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-instance-storage-config.html
    """

    write_parameter("connect", "associate-instance-storage-config")