#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-token.html
if __name__ == '__main__':
    """
	create-token : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-token.html
	list-tokens : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-tokens.html
    """

    parameter_display_string = """
    # token-id : Token ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("license-manager", "delete-token", "token-id", add_option_dict)





