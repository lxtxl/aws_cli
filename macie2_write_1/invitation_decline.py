#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/decline-invitations.html
if __name__ == '__main__':
    """
	accept-invitation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/accept-invitation.html
	create-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-invitations.html
	delete-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-invitations.html
	list-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-invitations.html
    """

    parameter_display_string = """
    # account-ids : An array that lists AWS account IDs, one for each account that sent an invitation to decline.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("macie2", "decline-invitations", "account-ids", add_option_dict)





