#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-group-members.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-id : The identifier for the organization under which the group exists.
    # group-id : The identifier for the group to which the members (users or groups) are associated.
    """

    execute_two_parameter("workmail", "list-group-members", "organization-id", "group-id", parameter_display_string)