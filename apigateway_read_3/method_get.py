#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-method.html
if __name__ == '__main__':
    """
	delete-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-method.html
	put-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-method.html
	update-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-method.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # resource-id : [Required] The  Resource identifier for the  Method resource.
    """

    execute_two_parameter("apigateway", "get-method", "rest-api-id", "resource-id", parameter_display_string)