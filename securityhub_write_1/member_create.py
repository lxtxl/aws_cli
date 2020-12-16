#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-members.html
if __name__ == '__main__':
    """
	delete-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-members.html
	disassociate-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disassociate-members.html
	get-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-members.html
	invite-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/invite-members.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-members.html
    """

    parameter_display_string = """
    # account-details : The list of accounts to associate with the Security Hub master account. For each account, the list includes the account ID and optionally the email address.
(structure)

The details of an AWS account.
AccountId -> (string)

The ID of an AWS account.

Email -> (string)

The email of an AWS account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("securityhub", "create-members", "account-details", add_option_dict)





