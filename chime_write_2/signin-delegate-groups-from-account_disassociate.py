#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/disassociate-signin-delegate-groups-from-account.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # group-names : The sign-in delegate group names.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "disassociate-signin-delegate-groups-from-account", "account-id", "group-names", add_option_dict)
