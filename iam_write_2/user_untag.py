#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user.html
	get-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-users.html
	tag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-user.html
    """

    parameter_display_string = """
    # user-name : The name of the IAM user from which you want to remove tags.
This parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
    # tag-keys : A list of key names as a simple array of strings. The tags with matching keys are removed from the specified user.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "untag-user", "user-name", "tag-keys", add_option_dict)
