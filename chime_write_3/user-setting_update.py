#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user-settings.html
if __name__ == '__main__':
    """
	get-user-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-user-settings.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # user-id : The user ID.
    # user-settings : The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.
(structure)

Describes an action and whether the action is enabled or disabled for users during their streaming sessions.
Action -> (string)

The action that is enabled or disabled.

Permission -> (string)

Indicates whether the action is enabled or disabled.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("chime", "update-user-settings", "account-id", "user-id", "user-settings", add_option_dict)
