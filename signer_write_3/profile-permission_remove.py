#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/remove-profile-permission.html
if __name__ == '__main__':
    """
	add-profile-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/add-profile-permission.html
	list-profile-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-profile-permissions.html
    """

    parameter_display_string = """
    # profile-name : A human-readable name for the signing profile with permissions to be removed.
    # revision-id : An identifier for the current revision of the signing profile permissions.
    # statement-id : A unique identifier for the cross-account permissions statement.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("signer", "remove-profile-permission", "profile-name", "revision-id", "statement-id", add_option_dict)
