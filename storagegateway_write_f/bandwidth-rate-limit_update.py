#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-bandwidth-rate-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-bandwidth-rate-limit.html
	describe-bandwidth-rate-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-bandwidth-rate-limit.html
    """

    write_parameter("storagegateway", "update-bandwidth-rate-limit")