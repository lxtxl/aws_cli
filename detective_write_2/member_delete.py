#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/delete-members.html
if __name__ == '__main__':
    """
	create-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-members.html
	get-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/get-members.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-members.html
    """

    parameter_display_string = """
    # graph-arn : The ARN of the behavior graph to delete members from.
    # account-ids : The list of AWS account identifiers for the member accounts to delete from the behavior graph.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("detective", "delete-members", "graph-arn", "account-ids", add_option_dict)
