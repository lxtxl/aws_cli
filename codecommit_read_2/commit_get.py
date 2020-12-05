#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-commit.html
if __name__ == '__main__':
    """
	create-commit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-commit.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository to which the commit was made.
    # commit-id : The commit ID. Commit IDs are the full SHA ID of the commit.
    """

    execute_two_parameter("codecommit", "get-commit", "repository-name", "commit-id", parameter_display_string)