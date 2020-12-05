#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-smb-file-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-smb-file-share.html
	describe-smb-file-shares : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-smb-file-shares.html
    """

    write_parameter("storagegateway", "update-smb-file-share")