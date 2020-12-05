#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-sessions.html
if __name__ == '__main__':
    """
	expire-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/expire-session.html
    """

    parameter_display_string = """
    # stack-name : The name of the stack. This value is case-sensitive.
    # fleet-name : The name of the fleet. This value is case-sensitive.
    """

    execute_two_parameter("appstream", "describe-sessions", "stack-name", "fleet-name", parameter_display_string)