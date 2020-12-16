#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/put-signing-profile.html
if __name__ == '__main__':
    """
	cancel-signing-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/cancel-signing-profile.html
	get-signing-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/get-signing-profile.html
	list-signing-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-profiles.html
	revoke-signing-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/revoke-signing-profile.html
    """

    parameter_display_string = """
    # profile-name : The name of the signing profile to be created.
    # platform-id : The ID of the signing platform to be created.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("signer", "put-signing-profile", "profile-name", "platform-id", add_option_dict)
