#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/move-account.html
if __name__ == '__main__':
    """
	create-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-account.html
	describe-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-account.html
	list-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-accounts.html
    """

    parameter_display_string = """
    # account-id : The unique identifier (ID) of the account that you want to move.
The regex pattern for an account ID string requires exactly 12 digits.
    # source-parent-id : The unique identifier (ID) of the root or organizational unit that you want to move the account from.
The regex pattern for a parent ID string requires one of the following:

Root - A string that begins with âr-â followed by from 4 to 32 lowercase letters or digits.
Organizational unit (OU) - A string that begins with âou-â followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second â-â dash and from 8 to 32 additional lowercase letters or digits.
    # destination-parent-id : The unique identifier (ID) of the root or organizational unit that you want to move the account to.
The regex pattern for a parent ID string requires one of the following:

Root - A string that begins with âr-â followed by from 4 to 32 lowercase letters or digits.
Organizational unit (OU) - A string that begins with âou-â followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second â-â dash and from 8 to 32 additional lowercase letters or digits.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("organizations", "move-account", "account-id", "source-parent-id", "destination-parent-id", add_option_dict)
