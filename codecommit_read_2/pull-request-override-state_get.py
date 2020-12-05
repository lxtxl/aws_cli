#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request-override-state.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # pull-request-id : The ID of the pull request for which you want to get information about whether approval rules have been set aside (overridden).
    # revision-id : The system-generated ID of the revision for the pull request. To retrieve the most recent revision ID, use  GetPullRequest .
    """

    execute_two_parameter("codecommit", "get-pull-request-override-state", "pull-request-id", "revision-id", parameter_display_string)