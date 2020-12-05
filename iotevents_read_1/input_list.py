#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/describe-input.html
if __name__ == '__main__':
    """
	create-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/create-input.html
	delete-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/delete-input.html
	list-inputs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/list-inputs.html
	update-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/update-input.html
    """

    parameter_display_string = """
    # input-name : The name of the input.
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

    execute_one_parameter("iotevents", "describe-input", "input-name", add_option_dict)