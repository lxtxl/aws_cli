#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-access-key.html
if __name__ == '__main__':
    """
	create-access-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-access-key.html
	delete-access-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-access-key.html
	list-access-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-access-keys.html
    """

    parameter_display_string = """
    # access-key-id : The access key ID of the secret access key you want to update.
This parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
    # status : The status you want to assign to the secret access key. Active means that the key can be used for API calls to AWS, while Inactive means that the key cannot be used.
Possible values:

Active
Inactive
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "update-access-key", "access-key-id", "status", add_option_dict)
