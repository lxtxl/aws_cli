#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-ssh-public-key.html
if __name__ == '__main__':
    """
	get-ssh-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-ssh-public-key.html
	list-ssh-public-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-ssh-public-keys.html
	update-ssh-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-ssh-public-key.html
	upload-ssh-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-ssh-public-key.html
    """

    parameter_display_string = """
    # user-name : The name of the IAM user associated with the SSH public key.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # ssh-public-key-id : The unique identifier for the SSH public key.
This parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "delete-ssh-public-key", "user-name", "ssh-public-key-id", add_option_dict)
