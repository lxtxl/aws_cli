#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-integration.html
if __name__ == '__main__':
    """
	delete-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-integration.html
	put-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-integration.html
	update-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-integration.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # resource-id : [Required] Specifies a get integration requestâs resource identifier
    """

    execute_two_parameter("apigateway", "get-integration", "rest-api-id", "resource-id", parameter_display_string)