#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-connection.html
if __name__ == '__main__':
    """
	create-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-connection.html
	delete-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-connection.html
	get-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-connection.html
	get-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-connections.html
    """

    parameter_display_string = """
    # name : The name of the connection definition to update.
    # connection-input : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "update-connection", "name", "connection-input", add_option_dict)
