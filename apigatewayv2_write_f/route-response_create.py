#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-route-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-route-response.html
	get-route-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-route-response.html
	get-route-responses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-route-responses.html
	update-route-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-route-response.html
    """

    write_parameter("apigatewayv2", "create-route-response")