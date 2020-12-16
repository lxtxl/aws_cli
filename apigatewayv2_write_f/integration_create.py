#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-integration.html
	get-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integration.html
	get-integrations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integrations.html
	update-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-integration.html
    """

    write_parameter("apigatewayv2", "create-integration")