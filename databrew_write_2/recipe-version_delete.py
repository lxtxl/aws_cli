#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/delete-recipe-version.html
if __name__ == '__main__':
    """
	list-recipe-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-recipe-versions.html
    """

    parameter_display_string = """
    # name : The name of the recipe to be deleted.
    # recipe-version : The version of the recipe to be deleted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("databrew", "delete-recipe-version", "name", "recipe-version", add_option_dict)
