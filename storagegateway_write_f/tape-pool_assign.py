#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-tape-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tape-pool.html
	delete-tape-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape-pool.html
	list-tape-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-tape-pools.html
    """

    write_parameter("storagegateway", "assign-tape-pool")