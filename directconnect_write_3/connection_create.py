#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-connection.html
if __name__ == '__main__':
    """
	confirm-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-connection.html
	delete-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-connection.html
	describe-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-connections.html
    """

    parameter_display_string = """
    # location : The location of the connection.
    # bandwidth : The bandwidth of the connection.
    # connection-name : The name of the connection.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("directconnect", "create-connection", "location", "bandwidth", "connection-name", add_option_dict)
