#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-documentation-version.html
if __name__ == '__main__':
    """
	create-documentation-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-documentation-version.html
	delete-documentation-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-documentation-version.html
	get-documentation-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-documentation-versions.html
	update-documentation-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-documentation-version.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # documentation-version : [Required] The version identifier of the to-be-retrieved documentation snapshot.
    """

    execute_two_parameter("apigateway", "get-documentation-version", "rest-api-id", "documentation-version", parameter_display_string)