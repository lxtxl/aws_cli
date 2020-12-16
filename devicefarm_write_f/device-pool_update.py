#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-device-pool.html
	delete-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-device-pool.html
	get-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-device-pool.html
	list-device-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-device-pools.html
    """

    write_parameter("devicefarm", "update-device-pool")