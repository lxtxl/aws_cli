#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-recipe.html
if __name__ == '__main__':
    """
	create-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-recipe.html
	list-recipes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-recipes.html
	publish-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/publish-recipe.html
	update-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-recipe.html
    """

    parameter_display_string = """
    # name : The name of the recipe to be described.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("databrew", "describe-recipe", "name", add_option_dict)