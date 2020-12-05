#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-differences.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # repository-name : The name of the repository where you want to get differences.
    # after-commit-specifier : The branch, tag, HEAD, or other fully qualified reference used to identify a commit.
    """

    execute_two_parameter("codecommit", "get-differences", "repository-name", "after-commit-specifier", parameter_display_string)