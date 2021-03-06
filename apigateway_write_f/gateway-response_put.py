#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-gateway-response.html
	get-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-gateway-response.html
	get-gateway-responses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-gateway-responses.html
	update-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-gateway-response.html
    """

    write_parameter("apigateway", "put-gateway-response")