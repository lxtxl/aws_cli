#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/expire-session.html
if __name__ == '__main__':
    """
	describe-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-sessions.html
    """

    parameter_display_string = """
    # session-id : The identifier of the streaming session.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appstream", "expire-session", "session-id", add_option_dict)





