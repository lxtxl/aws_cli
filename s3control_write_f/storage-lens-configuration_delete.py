#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-storage-lens-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration.html
	list-storage-lens-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-storage-lens-configurations.html
	put-storage-lens-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-storage-lens-configuration.html
    """

    write_parameter("s3control", "delete-storage-lens-configuration")