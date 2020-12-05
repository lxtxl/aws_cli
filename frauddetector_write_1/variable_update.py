#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-variable.html
if __name__ == '__main__':
    """
	create-variable : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-variable.html
	delete-variable : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-variable.html
	get-variables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-variables.html
    """

    parameter_display_string = """
    # name : The name of the variable.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("frauddetector", "update-variable", "name", add_option_dict)





