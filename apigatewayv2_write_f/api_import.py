#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-api.html
	delete-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-api.html
	export-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/export-api.html
	get-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api.html
	get-apis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-apis.html
	reimport-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/reimport-api.html
	update-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api.html
    """

    write_parameter("apigatewayv2", "import-api")