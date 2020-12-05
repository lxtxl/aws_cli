#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-user.html
	invite-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/invite-users.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-users.html
	logout-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/logout-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # user-id : The user ID.
    """

    execute_two_parameter("chime", "get-user", "account-id", "user-id", parameter_display_string)