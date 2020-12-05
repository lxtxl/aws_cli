#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/update-number-of-domain-controllers.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # directory-id : Identifier of the directory to which the domain controllers will be added or removed.
    # desired-number : The number of domain controllers desired in the directory.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "update-number-of-domain-controllers", "directory-id", "desired-number", add_option_dict)
