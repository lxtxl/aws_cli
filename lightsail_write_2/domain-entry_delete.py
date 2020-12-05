#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-domain-entry.html
if __name__ == '__main__':
    """
	create-domain-entry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-domain-entry.html
	update-domain-entry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/update-domain-entry.html
    """

    parameter_display_string = """
    # domain-name : The name of the domain entry to delete.
    # domain-entry : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "delete-domain-entry", "domain-name", "domain-entry", add_option_dict)
