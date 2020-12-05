#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-account.html
if __name__ == '__main__':
    """
	create-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-account.html
	list-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-accounts.html
	move-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/move-account.html
    """

    parameter_display_string = """
    # account-id : The unique identifier (ID) of the AWS account that you want information about. You can get the ID from the  ListAccounts or  ListAccountsForParent operations.
The regex pattern for an account ID string requires exactly 12 digits.
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

    execute_one_parameter("organizations", "describe-account", "account-id", add_option_dict)