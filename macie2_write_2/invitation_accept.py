#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/accept-invitation.html
if __name__ == '__main__':
    """
	create-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-invitations.html
	decline-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/decline-invitations.html
	delete-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-invitations.html
	list-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-invitations.html
    """

    parameter_display_string = """
    # invitation-id : The unique identifier for the invitation to accept.
    # master-account : The AWS account ID for the account that sent the invitation.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("macie2", "accept-invitation", "invitation-id", "master-account", add_option_dict)
