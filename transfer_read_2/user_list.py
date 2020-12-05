#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/delete-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/list-users.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/update-user.html
    """

    parameter_display_string = """
    # server-id : A system-assigned unique identifier for a server that has this user assigned.
    # user-name : The name of the user assigned to one or more servers. User names are part of the sign-in credentials to use the AWS Transfer Family service and perform file transfer tasks.
    """

    execute_two_parameter("transfer", "describe-user", "server-id", "user-name", parameter_display_string)