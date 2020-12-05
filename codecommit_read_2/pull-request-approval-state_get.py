#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request-approval-states.html
if __name__ == '__main__':
    """
	update-pull-request-approval-state : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-approval-state.html
    """

    parameter_display_string = """
    # pull-request-id : The system-generated ID for the pull request.
    # revision-id : The system-generated ID for the pull request revision.
    """

    execute_two_parameter("codecommit", "get-pull-request-approval-states", "pull-request-id", "revision-id", parameter_display_string)