#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-integration-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-integration-response.html
	delete-integration-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-integration-response.html
	get-integration-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integration-response.html
	get-integration-responses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integration-responses.html
    """

    write_parameter("apigatewayv2", "update-integration-response")