#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-mailbox-details.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-id : The identifier for the organization that contains the user whose mailbox details are being requested.
    # user-id : The identifier for the user whose mailbox details are being requested.
    """

    execute_two_parameter("workmail", "get-mailbox-details", "organization-id", "user-id", parameter_display_string)