#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-gateway-response.html
if __name__ == '__main__':
    """
	delete-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-gateway-response.html
	get-gateway-responses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-gateway-responses.html
	put-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-gateway-response.html
	update-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-gateway-response.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # response-type : [Required]
The response type of the associated  GatewayResponse . Valid values are

ACCESS_DENIED
API_CONFIGURATION_ERROR
AUTHORIZER_FAILURE
AUTHORIZER_CONFIGURATION_ERROR
BAD_REQUEST_PARAMETERS
BAD_REQUEST_BODY
DEFAULT_4XX
DEFAULT_5XX
EXPIRED_TOKEN
INVALID_SIGNATURE
INTEGRATION_FAILURE
INTEGRATION_TIMEOUT
INVALID_API_KEY
MISSING_AUTHENTICATION_TOKEN
QUOTA_EXCEEDED
REQUEST_TOO_LARGE
RESOURCE_NOT_FOUND
THROTTLED
UNAUTHORIZED
UNSUPPORTED_MEDIA_TYPE

Possible values:

DEFAULT_4XX
DEFAULT_5XX
RESOURCE_NOT_FOUND
UNAUTHORIZED
INVALID_API_KEY
ACCESS_DENIED
AUTHORIZER_FAILURE
AUTHORIZER_CONFIGURATION_ERROR
INVALID_SIGNATURE
EXPIRED_TOKEN
MISSING_AUTHENTICATION_TOKEN
INTEGRATION_FAILURE
INTEGRATION_TIMEOUT
API_CONFIGURATION_ERROR
UNSUPPORTED_MEDIA_TYPE
BAD_REQUEST_PARAMETERS
BAD_REQUEST_BODY
REQUEST_TOO_LARGE
THROTTLED
QUOTA_EXCEEDED
    """

    execute_two_parameter("apigateway", "get-gateway-response", "rest-api-id", "response-type", parameter_display_string)