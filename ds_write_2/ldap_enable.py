#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/enable-ldaps.html
if __name__ == '__main__':
    """
	disable-ldaps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/disable-ldaps.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory.
    # type : The type of LDAP security to enable. Currently only the value Client is supported.
Possible values:

Client
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "enable-ldaps", "directory-id", "type", add_option_dict)
