#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-connection-alias.html
if __name__ == '__main__':
    """
	associate-connection-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/associate-connection-alias.html
	create-connection-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-connection-alias.html
	disassociate-connection-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/disassociate-connection-alias.html
    """

    parameter_display_string = """
    # alias-id : The identifier of the connection alias to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workspaces", "delete-connection-alias", "alias-id", add_option_dict)





