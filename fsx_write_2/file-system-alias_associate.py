#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/associate-file-system-aliases.html
if __name__ == '__main__':
    """
	describe-file-system-aliases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-file-system-aliases.html
	disassociate-file-system-aliases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/disassociate-file-system-aliases.html
    """

    parameter_display_string = """
    # file-system-id : Specifies the file system with which you want to associate one or more DNS aliases.
    # aliases : An array of one or more DNS alias names to associate with the file system. The alias name has to comply with the following formatting requirements:

Formatted as a fully-qualified domain name (FQDN), * hostname.domain * , for example, accounting.corp.example.com .
Can contain alphanumeric characters and the hyphen (-).
Cannot start or end with a hyphen.
Can start with a numeric.

For DNS alias names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("fsx", "associate-file-system-aliases", "file-system-id", "aliases", add_option_dict)
