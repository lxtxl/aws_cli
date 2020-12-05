#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/disassociate-file-system-aliases.html
if __name__ == '__main__':
    """
	associate-file-system-aliases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/associate-file-system-aliases.html
	describe-file-system-aliases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-file-system-aliases.html
    """

    parameter_display_string = """
    # file-system-id : Specifies the file system from which to disassociate the DNS aliases.
    # aliases : An array of one or more DNS alias names to disassociate, or remove, from the file system.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("fsx", "disassociate-file-system-aliases", "file-system-id", "aliases", add_option_dict)
