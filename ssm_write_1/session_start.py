#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-session.html
if __name__ == '__main__':
    """
	describe-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-sessions.html
	resume-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/resume-session.html
	terminate-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/terminate-session.html
    """

    parameter_display_string = """
    # target : The instance to connect to for the session.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "start-session", "target", add_option_dict)





