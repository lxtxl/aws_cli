#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/associate-signin-delegate-groups-with-account.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # signin-delegate-groups : The sign-in delegate groups.
(structure)

An Active Directory (AD) group whose members are granted permission to act as delegates.
GroupName -> (string)

The group name.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "associate-signin-delegate-groups-with-account", "account-id", "signin-delegate-groups", add_option_dict)
