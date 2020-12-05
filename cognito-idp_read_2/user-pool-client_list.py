#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool-client.html
if __name__ == '__main__':
    """
	create-user-pool-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-client.html
	delete-user-pool-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool-client.html
	list-user-pool-clients : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pool-clients.html
	update-user-pool-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool-client.html
    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool you want to describe.
    # client-id : The app client ID of the app associated with the user pool.
    """

    execute_two_parameter("cognito-idp", "describe-user-pool-client", "user-pool-id", "client-id", parameter_display_string)