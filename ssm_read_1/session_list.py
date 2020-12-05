#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-sessions.html
if __name__ == '__main__':
    """
	resume-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/resume-session.html
	start-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-session.html
	terminate-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/terminate-session.html
    """

    parameter_display_string = """
    # state : The session status to retrieve a list of sessions for. For example, âActiveâ.
Possible values:

Active
History
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

    execute_one_parameter("ssm", "describe-sessions", "state", add_option_dict)