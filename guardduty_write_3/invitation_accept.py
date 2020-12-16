#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/accept-invitation.html
if __name__ == '__main__':
    """
	decline-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/decline-invitations.html
	delete-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-invitations.html
	list-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-invitations.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector of the GuardDuty member account.
    # master-id : The account ID of the master GuardDuty account whose invitation youâre accepting.
    # invitation-id : The value that is used to validate the master account to the member account.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("guardduty", "accept-invitation", "detector-id", "master-id", "invitation-id", add_option_dict)
