#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/delete-ssh-public-key.html
if __name__ == '__main__':
    """
	import-ssh-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/import-ssh-public-key.html
    """

    parameter_display_string = """
    # server-id : A system-assigned unique identifier for a file transfer protocol-enabled server instance that has the user assigned to it.
    # ssh-public-key-id : A unique identifier used to reference your userâs specific SSH key.
    # user-name : A unique string that identifies a user whose public key is being deleted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("transfer", "delete-ssh-public-key", "server-id", "ssh-public-key-id", "user-name", add_option_dict)
