#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-get-commits.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # commit-ids : The full commit IDs of the commits to get information about.

Note
You must supply the full SHA IDs of each commit. You cannot use shortened SHA IDs.

(string)
    # repository-name : The name of the repository that contains the commits.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "batch-get-commits", "commit-ids", "repository-name", add_option_dict)
