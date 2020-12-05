#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-slot-type-version.html
if __name__ == '__main__':
    """
	create-slot-type-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-slot-type-version.html
	get-slot-type-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-slot-type-versions.html
    """

    parameter_display_string = """
    # name : The name of the slot type.
    # slot-type-version : The version of the slot type to delete. You cannot delete the $LATEST version of the slot type. To delete the $LATEST version, use the  DeleteSlotType operation.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lex-models", "delete-slot-type-version", "name", "slot-type-version", add_option_dict)
