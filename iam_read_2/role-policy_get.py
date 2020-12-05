#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role-policy.html
if __name__ == '__main__':
    """
	attach-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html
	delete-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role-policy.html
	detach-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-role-policy.html
	list-role-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-role-policies.html
	put-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-role-policy.html
    """

    parameter_display_string = """
    # role-name : The name of the role associated with the policy.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # policy-name : The name of the policy document to get.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """

    execute_two_parameter("iam", "get-role-policy", "role-name", "policy-name", parameter_display_string)