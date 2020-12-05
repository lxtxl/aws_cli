#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/update-server.html
if __name__ == '__main__':
    """
	create-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/create-server.html
	delete-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/delete-server.html
	describe-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-server.html
	list-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/list-servers.html
	start-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/start-server.html
	stop-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/stop-server.html
    """

    parameter_display_string = """
    # server-id : A system-assigned unique identifier for a server instance that the user account is assigned to.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("transfer", "update-server", "server-id", add_option_dict)





