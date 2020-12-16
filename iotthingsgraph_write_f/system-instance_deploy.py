#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/create-system-instance.html
	delete-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-system-instance.html
	get-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-system-instance.html
	search-system-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-system-instances.html
	undeploy-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/undeploy-system-instance.html
    """

    write_parameter("iotthingsgraph", "deploy-system-instance")