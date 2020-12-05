#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-connection.html
if __name__ == '__main__':
    """
	delete-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-connection.html
	get-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-connection.html
	list-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-connections.html
    """

    parameter_display_string = """
    # connection-name : The name of the connection to be created. The name must be unique in the calling AWS account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codestar-connections", "create-connection", "connection-name", add_option_dict)





