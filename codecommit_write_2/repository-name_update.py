#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-repository-name.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # old-name : The current name of the repository.
    # new-name : The new name for the repository.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "update-repository-name", "old-name", "new-name", add_option_dict)
