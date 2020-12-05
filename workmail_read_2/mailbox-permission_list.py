#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mailbox-permissions.html
if __name__ == '__main__':
    """
	delete-mailbox-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-mailbox-permissions.html
	put-mailbox-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-mailbox-permissions.html
    """

    parameter_display_string = """
    # organization-id : The identifier of the organization under which the user, group, or resource exists.
    # entity-id : The identifier of the user, group, or resource for which to list mailbox permissions.
    """

    execute_two_parameter("workmail", "list-mailbox-permissions", "organization-id", "entity-id", parameter_display_string)