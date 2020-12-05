#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-connection.html
if __name__ == '__main__':
    """
	create-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-connection.html
	get-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-connection.html
	list-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-connections.html
    """

    parameter_display_string = """
    # connection-arn : The Amazon Resource Name (ARN) of the connection to be deleted.

Note
The ARN is never reused if the connection is deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codestar-connections", "delete-connection", "connection-arn", add_option_dict)





