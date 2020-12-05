#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-configuration-set.html
if __name__ == '__main__':
    """
	create-configuration-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-configuration-set.html
	delete-configuration-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-configuration-set.html
	list-configuration-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-configuration-sets.html
    """

    parameter_display_string = """
    # configuration-set-name : The name of the configuration set that you want to obtain more information about.
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

    execute_one_parameter("sesv2", "get-configuration-set", "configuration-set-name", add_option_dict)