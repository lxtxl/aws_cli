#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/invite-users.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-user.html
	get-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-users.html
	logout-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/logout-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # user-email-list : The user email addresses to which to send the email invitation.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "invite-users", "account-id", "user-email-list", add_option_dict)
