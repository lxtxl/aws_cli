#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/import-key-pair.html
if __name__ == '__main__':
    """
	create-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-key-pair.html
	delete-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-key-pair.html
	get-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-key-pair.html
	get-key-pairs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-key-pairs.html
    """

    parameter_display_string = """
    # key-pair-name : The name of the key pair for which you want to import the public key.
    # public-key-base64 : A base64-encoded public key of the ssh-rsa type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "import-key-pair", "key-pair-name", "public-key-base64", add_option_dict)
