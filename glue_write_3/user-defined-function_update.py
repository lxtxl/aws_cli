#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-user-defined-function.html
if __name__ == '__main__':
    """
	create-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-user-defined-function.html
	delete-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-user-defined-function.html
	get-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-user-defined-function.html
	get-user-defined-functions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-user-defined-functions.html
    """

    parameter_display_string = """
    # database-name : The name of the catalog database where the function to be updated is located.
    # function-name : The name of the function.
    # function-input : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "update-user-defined-function", "database-name", "function-name", "function-input", add_option_dict)
