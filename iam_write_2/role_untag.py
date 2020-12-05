#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-role.html
if __name__ == '__main__':
    """
	create-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html
	delete-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role.html
	get-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role.html
	list-roles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-roles.html
	tag-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-role.html
	update-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-role.html
    """

    parameter_display_string = """
    # role-name : The name of the IAM role from which you want to remove tags.
This parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # tag-keys : A list of key names as a simple array of strings. The tags with matching keys are removed from the specified role.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "untag-role", "role-name", "tag-keys", add_option_dict)
