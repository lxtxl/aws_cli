#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-intent-version.html
if __name__ == '__main__':
    """
	delete-intent-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-intent-version.html
	get-intent-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-intent-versions.html
    """

    parameter_display_string = """
    # name : The name of the intent that you want to create a new version of. The name is case sensitive.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lex-models", "create-intent-version", "name", add_option_dict)





