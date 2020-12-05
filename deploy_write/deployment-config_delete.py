#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-deployment-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-config.html
	get-deployment-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-config.html
	list-deployment-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-configs.html
    """

    write_parameter("deploy", "delete-deployment-config")