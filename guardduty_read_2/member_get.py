#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-members.html
if __name__ == '__main__':
    """
	create-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-members.html
	delete-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-members.html
	disassociate-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/disassociate-members.html
	invite-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/invite-members.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-members.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector of the GuardDuty account whose members you want to retrieve.
    # account-ids : A list of account IDs of the GuardDuty member accounts that you want to describe.
(string)
    """

    execute_two_parameter("guardduty", "get-members", "detector-id", "account-ids", parameter_display_string)