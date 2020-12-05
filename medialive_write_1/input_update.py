#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-input.html
if __name__ == '__main__':
    """
	create-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-input.html
	delete-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-input.html
	describe-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-input.html
	list-inputs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-inputs.html
    """

    parameter_display_string = """
    # input-id : Unique ID of the input.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("medialive", "update-input", "input-id", add_option_dict)





