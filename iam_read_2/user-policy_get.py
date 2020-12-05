#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user-policy.html
if __name__ == '__main__':
    """
	attach-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html
	delete-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-policy.html
	detach-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-user-policy.html
	list-user-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-policies.html
	put-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-policy.html
    """

    parameter_display_string = """
    # user-name : The name of the user who the policy is associated with.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # policy-name : The name of the policy document to get.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """

    execute_two_parameter("iam", "get-user-policy", "user-name", "policy-name", parameter_display_string)