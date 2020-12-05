#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/batch-delete-recipe-version.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # name : The name of the recipe to be modified.
    # recipe-versions : An array of version identifiers to be deleted.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("databrew", "batch-delete-recipe-version", "name", "recipe-versions", add_option_dict)
