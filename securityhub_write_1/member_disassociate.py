#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disassociate-members.html
if __name__ == '__main__':
    """
	create-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-members.html
	delete-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-members.html
	get-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-members.html
	invite-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/invite-members.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-members.html
    """

    parameter_display_string = """
    # account-ids : The account IDs of the member accounts to disassociate from the master account.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("securityhub", "disassociate-members", "account-ids", add_option_dict)





