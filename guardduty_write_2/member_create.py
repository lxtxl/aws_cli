#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-members.html
if __name__ == '__main__':
    """
	delete-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-members.html
	disassociate-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/disassociate-members.html
	get-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-members.html
	invite-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/invite-members.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-members.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector of the GuardDuty account that you want to associate member accounts with.
    # account-details : A list of account ID and email address pairs of the accounts that you want to associate with the master GuardDuty account.
(structure)

Contains information about the account.
AccountId -> (string)

The member account ID.

Email -> (string)

The email address of the member account.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "create-members", "detector-id", "account-details", add_option_dict)
