#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-security-key.html
if __name__ == '__main__':
    """
	disassociate-security-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-security-key.html
	list-security-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-security-keys.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # key : A valid security key in PEM format.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connect", "associate-security-key", "instance-id", "key", add_option_dict)
