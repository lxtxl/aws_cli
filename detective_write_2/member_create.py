#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-members.html
if __name__ == '__main__':
    """
	delete-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/delete-members.html
	get-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/get-members.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-members.html
    """

    parameter_display_string = """
    # graph-arn : The ARN of the behavior graph to invite the member accounts to contribute their data to.
    # accounts : The list of AWS accounts to invite to become member accounts in the behavior graph. For each invited account, the account list contains the account identifier and the AWS account root user email address.
(structure)

An AWS account that is the master of or a member of a behavior graph.
AccountId -> (string)

The account identifier of the AWS account.

EmailAddress -> (string)

The AWS account root user email address for the AWS account.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("detective", "create-members", "graph-arn", "accounts", add_option_dict)
