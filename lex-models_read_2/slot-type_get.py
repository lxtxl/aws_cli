#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-slot-type.html
if __name__ == '__main__':
    """
	delete-slot-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-slot-type.html
	get-slot-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-slot-types.html
	put-slot-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-slot-type.html
    """

    parameter_display_string = """
    # name : The name of the slot type. The name is case sensitive.
    # slot-type-version : The version of the slot type.
    """

    execute_two_parameter("lex-models", "get-slot-type", "name", "slot-type-version", parameter_display_string)