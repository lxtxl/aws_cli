#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	continue-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/continue-deployment.html
	create-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment.html
	get-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment.html
	list-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployments.html
    """

    write_parameter("deploy", "stop-deployment")