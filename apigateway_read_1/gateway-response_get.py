#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-gateway-responses.html
if __name__ == '__main__':
    """
	delete-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-gateway-response.html
	get-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-gateway-response.html
	put-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-gateway-response.html
	update-gateway-response : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-gateway-response.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("apigateway", "get-gateway-responses", "rest-api-id", add_option_dict)