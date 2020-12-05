#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-group.html
if __name__ == '__main__':
    """
	create-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-group.html
	delete-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-groups.html
    """

    parameter_display_string = """
    # organization-id : The identifier for the organization under which the group exists.
    # group-id : The identifier for the group to be described.
    """

    execute_two_parameter("workmail", "describe-group", "organization-id", "group-id", parameter_display_string)