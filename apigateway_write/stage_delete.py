#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-stage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-stage.html
	get-stage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-stage.html
	get-stages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-stages.html
	update-stage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-stage.html
    """

    write_parameter("apigateway", "delete-stage")