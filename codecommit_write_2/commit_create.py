#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-commit.html
if __name__ == '__main__':
    """
	get-commit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-commit.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository where you create the commit.
    # branch-name : The name of the branch where you create the commit.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "create-commit", "repository-name", "branch-name", add_option_dict)
