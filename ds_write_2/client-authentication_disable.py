#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/disable-client-authentication.html
if __name__ == '__main__':
    """
	enable-client-authentication : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/enable-client-authentication.html
    """

    parameter_display_string = """
    # directory-id : Disable client authentication in a specified directory for smart cards.
    # type : Disable the type of client authentication request.
Possible values:

SmartCard
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "disable-client-authentication", "directory-id", "type", add_option_dict)
