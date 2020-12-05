#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-pull-request-by-fast-forward.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # pull-request-id : The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
    # repository-name : The name of the repository where the pull request was created.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "merge-pull-request-by-fast-forward", "pull-request-id", "repository-name", add_option_dict)
