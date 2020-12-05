#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-user-defined-functions.html
if __name__ == '__main__':
    """
	create-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-user-defined-function.html
	delete-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-user-defined-function.html
	get-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-user-defined-function.html
	update-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-user-defined-function.html
    """

    parameter_display_string = """
    # pattern : An optional function-name pattern string that filters the function definitions returned.
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

    execute_one_parameter("glue", "get-user-defined-functions", "pattern", add_option_dict)