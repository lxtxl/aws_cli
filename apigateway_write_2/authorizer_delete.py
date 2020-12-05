#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-authorizer.html
if __name__ == '__main__':
    """
	create-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-authorizer.html
	get-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-authorizer.html
	get-authorizers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-authorizers.html
	update-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-authorizer.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # authorizer-id : [Required] The identifier of the  Authorizer resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "delete-authorizer", "rest-api-id", "authorizer-id", add_option_dict)
