#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role-policy.html
if __name__ == '__main__':
    """
	attach-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html
	detach-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-role-policy.html
	get-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role-policy.html
	list-role-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-role-policies.html
	put-role-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-role-policy.html
    """

    parameter_display_string = """
    # role-name : The name (friendly name, not ARN) identifying the role that the policy is embedded in.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # policy-name : The name of the inline policy to delete from the specified IAM role.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "delete-role-policy", "role-name", "policy-name", add_option_dict)
