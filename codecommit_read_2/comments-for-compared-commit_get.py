#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comments-for-compared-commit.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # repository-name : The name of the repository where you want to compare commits.
    # after-commit-id : To establish the directionality of the comparison, the full commit ID of the after commit.
    """

    execute_two_parameter("codecommit", "get-comments-for-compared-commit", "repository-name", "after-commit-id", parameter_display_string)