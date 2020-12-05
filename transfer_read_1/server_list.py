#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-server.html
if __name__ == '__main__':
    """
	create-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/create-server.html
	delete-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/delete-server.html
	list-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/list-servers.html
	start-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/start-server.html
	stop-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/stop-server.html
	update-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/update-server.html
    """

    parameter_display_string = """
    # server-id : A system-assigned unique identifier for a server.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("transfer", "describe-server", "server-id", add_option_dict)