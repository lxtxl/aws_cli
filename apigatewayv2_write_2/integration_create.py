#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-integration.html
if __name__ == '__main__':
    """
	delete-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-integration.html
	get-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integration.html
	get-integrations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integrations.html
	update-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-integration.html
    """

    parameter_display_string = """
    # api-id : The API identifier.
    # integration-type : The integration type of an integration. One of the following:
AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.
AWS_PROXY: for integrating the route or method request with a Lambda function or other AWS service action. This integration is also referred to as a Lambda proxy integration.
HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.
HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an HTTP_PROXY integration.
MOCK: for integrating the route or method request with API Gateway as a âloopbackâ endpoint without invoking any backend. Supported only for WebSocket APIs.
Possible values:

AWS
HTTP
MOCK
HTTP_PROXY
AWS_PROXY
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigatewayv2", "create-integration", "api-id", "integration-type", add_option_dict)
