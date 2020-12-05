#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-slot-type.html
if __name__ == '__main__':
    """
	delete-slot-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-slot-type.html
	get-slot-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-slot-type.html
	get-slot-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-slot-types.html
    """

    parameter_display_string = """
    # name : The name of the slot type. The name is not case sensitive.
The name canât match a built-in slot type name, or a built-in slot type name with âAMAZON.â removed. For example, because there is a built-in slot type called AMAZON.DATE , you canât create a custom slot type called DATE .
For a list of built-in slot types, see Slot Type Reference in the Alexa Skills Kit .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lex-models", "put-slot-type", "name", add_option_dict)





