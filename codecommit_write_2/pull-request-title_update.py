#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-title.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # pull-request-id : The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
    # title : The updated title of the pull request. This replaces the existing title.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "update-pull-request-title", "pull-request-id", "title", add_option_dict)
