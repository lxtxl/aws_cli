#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/enable-client-authentication.html
if __name__ == '__main__':
    """
	disable-client-authentication : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/disable-client-authentication.html
    """

    parameter_display_string = """
    # directory-id : Enable client authentication in a specified directory for smart cards.
    # type : Enable the type of client authentication request.
Possible values:

SmartCard
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "enable-client-authentication", "directory-id", "type", add_option_dict)
