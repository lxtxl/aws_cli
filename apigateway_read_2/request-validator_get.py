#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-request-validator.html
if __name__ == '__main__':
    """
	create-request-validator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-request-validator.html
	delete-request-validator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-request-validator.html
	get-request-validators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-request-validators.html
	update-request-validator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-request-validator.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # request-validator-id : [Required] The identifier of the  RequestValidator to be retrieved.
    """

    execute_two_parameter("apigateway", "get-request-validator", "rest-api-id", "request-validator-id", parameter_display_string)