#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-request-validator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-request-validator.html
	delete-request-validator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-request-validator.html
	get-request-validator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-request-validator.html
	get-request-validators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-request-validators.html
    """

    write_parameter("apigateway", "update-request-validator")