#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-integration.html
	get-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-integration.html
	put-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-integration.html
    """

    write_parameter("apigateway", "update-integration")