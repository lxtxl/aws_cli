#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-invitations.html
if __name__ == '__main__':
    """
	accept-invitation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/accept-invitation.html
	create-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-invitations.html
	decline-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/decline-invitations.html
	delete-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-invitations.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("macie2", "list-invitations", add_option_dict)