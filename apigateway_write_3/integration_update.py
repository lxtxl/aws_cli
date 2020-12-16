#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-integration.html
if __name__ == '__main__':
    """
	delete-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-integration.html
	get-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-integration.html
	put-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-integration.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # resource-id : [Required] Represents an update integration requestâs resource identifier.
    # http-method : [Required] Represents an update integration requestâs HTTP method.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("apigateway", "update-integration", "rest-api-id", "resource-id", "http-method", add_option_dict)
