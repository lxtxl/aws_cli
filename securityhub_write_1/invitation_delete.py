#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-invitations.html
if __name__ == '__main__':
    """
	accept-invitation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/accept-invitation.html
	decline-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/decline-invitations.html
	list-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-invitations.html
    """

    parameter_display_string = """
    # account-ids : The list of the account IDs that sent the invitations to delete.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("securityhub", "delete-invitations", "account-ids", add_option_dict)





