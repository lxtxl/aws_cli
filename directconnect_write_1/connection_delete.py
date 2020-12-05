#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-connection.html
if __name__ == '__main__':
    """
	confirm-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-connection.html
	create-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-connection.html
	describe-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-connections.html
    """

    parameter_display_string = """
    # connection-id : The ID of the connection.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("directconnect", "delete-connection", "connection-id", add_option_dict)





