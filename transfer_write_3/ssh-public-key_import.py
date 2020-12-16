#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/import-ssh-public-key.html
if __name__ == '__main__':
    """
	delete-ssh-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/delete-ssh-public-key.html
    """

    parameter_display_string = """
    # server-id : A system-assigned unique identifier for a server.
    # ssh-public-key-body : The public key portion of an SSH key pair.
    # user-name : The name of the user account that is assigned to one or more servers.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("transfer", "import-ssh-public-key", "server-id", "ssh-public-key-body", "user-name", add_option_dict)
