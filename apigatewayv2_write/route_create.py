#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-route.html
	get-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-route.html
	get-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-routes.html
	update-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-route.html
    """

    write_parameter("apigatewayv2", "create-route")