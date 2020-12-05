#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-authorizer.html
	get-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-authorizer.html
	get-authorizers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-authorizers.html
	update-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-authorizer.html
    """

    write_parameter("apigateway", "delete-authorizer")