#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-user.html
if __name__ == '__main__':
    """
	get-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-user.html
	invite-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/invite-users.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-users.html
	logout-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/logout-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "create-user", "account-id", add_option_dict)





