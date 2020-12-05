#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group-policy.html
if __name__ == '__main__':
    """
	attach-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-group-policy.html
	delete-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group-policy.html
	detach-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-group-policy.html
	list-group-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-group-policies.html
	put-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-group-policy.html
    """

    parameter_display_string = """
    # group-name : The name of the group the policy is associated with.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # policy-name : The name of the policy document to get.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """

    execute_two_parameter("iam", "get-group-policy", "group-name", "policy-name", parameter_display_string)