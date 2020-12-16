#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-profile-permissions.html
if __name__ == '__main__':
    """
	add-profile-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/add-profile-permission.html
	remove-profile-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/remove-profile-permission.html
    """

    parameter_display_string = """
    # profile-name : Name of the signing profile containing the cross-account permissions.
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

    execute_one_parameter("signer", "list-profile-permissions", "profile-name", add_option_dict)