#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/disable-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-user.html
	describe-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-users.html
	enable-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/enable-user.html
    """

    parameter_display_string = """
    # user-name : The email address of the user.

Note
Usersâ email addresses are case-sensitive.
    # authentication-type : The authentication type for the user. You must specify USERPOOL.
Possible values:

API
SAML
USERPOOL
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appstream", "disable-user", "user-name", "authentication-type", add_option_dict)
