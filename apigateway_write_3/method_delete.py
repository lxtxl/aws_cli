#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-method.html
if __name__ == '__main__':
    """
	get-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-method.html
	put-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-method.html
	update-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-method.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # resource-id : [Required] The  Resource identifier for the  Method resource.
    # http-method : [Required] The HTTP verb of the  Method resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("apigateway", "delete-method", "rest-api-id", "resource-id", "http-method", add_option_dict)
