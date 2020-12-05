#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/update-input.html
if __name__ == '__main__':
    """
	create-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/create-input.html
	delete-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/delete-input.html
	describe-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/describe-input.html
	list-inputs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/list-inputs.html
    """

    parameter_display_string = """
    # input-name : The name of the input you want to update.
    # input-definition : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotevents", "update-input", "input-name", "input-definition", add_option_dict)
