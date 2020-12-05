#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-domain-name.html
	delete-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-domain-name.html
	get-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-domain-name.html
	get-domain-names : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-domain-names.html
    """

    write_parameter("apigatewayv2", "update-domain-name")