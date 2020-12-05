#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-deployment.html
	delete-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-deployment.html
	get-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-deployment.html
	get-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-deployments.html
    """

    write_parameter("apigateway", "update-deployment")