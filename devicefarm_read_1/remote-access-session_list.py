#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-remote-access-sessions.html
if __name__ == '__main__':
    """
	create-remote-access-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-remote-access-session.html
	delete-remote-access-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-remote-access-session.html
	get-remote-access-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-remote-access-session.html
	stop-remote-access-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/stop-remote-access-session.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the project about which you are requesting information.
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

    execute_one_parameter("devicefarm", "list-remote-access-sessions", "arn", add_option_dict)