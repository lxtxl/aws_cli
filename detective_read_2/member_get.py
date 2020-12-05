#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/get-members.html
if __name__ == '__main__':
    """
	create-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-members.html
	delete-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/delete-members.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-members.html
    """

    parameter_display_string = """
    # graph-arn : The ARN of the behavior graph for which to request the member details.
    # account-ids : The list of AWS account identifiers for the member account for which to return member details.
You cannot use GetMembers to retrieve information about member accounts that were removed from the behavior graph.
(string)
    """

    execute_two_parameter("detective", "get-members", "graph-arn", "account-ids", parameter_display_string)