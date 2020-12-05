#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-resource-server.html
if __name__ == '__main__':
    """
	create-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-resource-server.html
	delete-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-resource-server.html
	list-resource-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-resource-servers.html
	update-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-resource-server.html
    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool that hosts the resource server.
    # identifier : The identifier for the resource server
    """

    execute_two_parameter("cognito-idp", "describe-resource-server", "user-pool-id", "identifier", parameter_display_string)