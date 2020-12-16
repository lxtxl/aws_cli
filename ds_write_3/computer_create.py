#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-computer.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # directory-id : The identifier of the directory in which to create the computer account.
    # computer-name : The name of the computer account.
    # password : A one-time password that is used to join the computer to the directory. You should generate a random, strong password to use for this parameter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ds", "create-computer", "directory-id", "computer-name", "password", add_option_dict)
