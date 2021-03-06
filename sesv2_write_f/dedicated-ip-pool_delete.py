#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-dedicated-ip-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-dedicated-ip-pool.html
	list-dedicated-ip-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-dedicated-ip-pools.html
    """

    write_parameter("sesv2", "delete-dedicated-ip-pool")