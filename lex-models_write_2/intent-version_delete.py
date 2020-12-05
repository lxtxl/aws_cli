#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-intent-version.html
if __name__ == '__main__':
    """
	create-intent-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-intent-version.html
	get-intent-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-intent-versions.html
    """

    parameter_display_string = """
    # name : The name of the intent.
    # intent-version : The version of the intent to delete. You cannot delete the $LATEST version of the intent. To delete the $LATEST version, use the  DeleteIntent operation.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lex-models", "delete-intent-version", "name", "intent-version", add_option_dict)
