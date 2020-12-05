#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/associate-connection-alias.html
if __name__ == '__main__':
    """
	create-connection-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-connection-alias.html
	delete-connection-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-connection-alias.html
	disassociate-connection-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/disassociate-connection-alias.html
    """

    parameter_display_string = """
    # alias-id : The identifier of the connection alias.
    # resource-id : The identifier of the directory to associate the connection alias with.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workspaces", "associate-connection-alias", "alias-id", "resource-id", add_option_dict)
