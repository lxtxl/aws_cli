#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-ssh-public-key.html
if __name__ == '__main__':
    """
	delete-ssh-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-ssh-public-key.html
	get-ssh-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-ssh-public-key.html
	list-ssh-public-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-ssh-public-keys.html
	update-ssh-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-ssh-public-key.html
    """

    parameter_display_string = """
    # user-name : The name of the IAM user to associate the SSH public key with.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # ssh-public-key-body : The SSH public key. The public key must be encoded in ssh-rsa format or PEM format. The minimum bit-length of the public key is 2048 bits. For example, you can generate a 2048-bit key, and the resulting PEM file is 1679 bytes long.
The regex pattern used to validate this parameter is a string of characters consisting of the following:

Any printable ASCII character ranging from the space character (\u0020 ) through the end of the ASCII character range
The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF )
The special characters tab (\u0009 ), line feed (\u000A ), and carriage return (\u000D )
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "upload-ssh-public-key", "user-name", "ssh-public-key-body", add_option_dict)
