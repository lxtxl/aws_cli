#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/accept-invitation.html
if __name__ == '__main__':
    """
	decline-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/decline-invitations.html
	delete-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-invitations.html
	list-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-invitations.html
    """

    parameter_display_string = """
    # master-id : The account ID of the Security Hub master account that sent the invitation.
    # invitation-id : The ID of the invitation sent from the Security Hub master account.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("securityhub", "accept-invitation", "master-id", "invitation-id", add_option_dict)
