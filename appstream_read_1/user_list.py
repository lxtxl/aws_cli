#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-users.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-user.html
	disable-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/disable-user.html
	enable-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/enable-user.html
    """

    parameter_display_string = """
    # authentication-type : The authentication type for the users in the user pool to describe. You must specify USERPOOL.
Possible values:

API
SAML
USERPOOL
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("appstream", "describe-users", "authentication-type", add_option_dict)