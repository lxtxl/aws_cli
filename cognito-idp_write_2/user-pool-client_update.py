#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool-client.html
if __name__ == '__main__':
    """
	create-user-pool-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-client.html
	delete-user-pool-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool-client.html
	describe-user-pool-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool-client.html
	list-user-pool-clients : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pool-clients.html
    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool where you want to update the user pool client.
    # client-id : The ID of the client associated with the user pool.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "update-user-pool-client", "user-pool-id", "client-id", add_option_dict)
