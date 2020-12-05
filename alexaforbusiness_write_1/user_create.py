#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-user.html
if __name__ == '__main__':
    """
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-user.html
	search-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-users.html
    """

    parameter_display_string = """
    # user-id : The ARN for the user.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "create-user", "user-id", add_option_dict)





