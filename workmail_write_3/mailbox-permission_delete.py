#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-mailbox-permissions.html
if __name__ == '__main__':
    """
	list-mailbox-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mailbox-permissions.html
	put-mailbox-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-mailbox-permissions.html
    """

    parameter_display_string = """
    # organization-id : The identifier of the organization under which the member (user or group) exists.
    # entity-id : The identifier of the member (user or group) that owns the mailbox.
    # grantee-id : The identifier of the member (user or group) for which to delete granted permissions.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workmail", "delete-mailbox-permissions", "organization-id", "entity-id", "grantee-id", add_option_dict)
