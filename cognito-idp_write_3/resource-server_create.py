#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-resource-server.html
if __name__ == '__main__':
    """
	delete-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-resource-server.html
	describe-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-resource-server.html
	list-resource-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-resource-servers.html
	update-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-resource-server.html
    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool.
    # identifier : A unique resource server identifier for the resource server. This could be an HTTPS endpoint where the resource server is located. For example, https://my-weather-api.example.com .
    # name : A friendly name for the resource server.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "create-resource-server", "user-pool-id", "identifier", "name", add_option_dict)
