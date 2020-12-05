#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-conditional-forwarders.html
if __name__ == '__main__':
    """
	create-conditional-forwarder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-conditional-forwarder.html
	delete-conditional-forwarder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-conditional-forwarder.html
	update-conditional-forwarder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/update-conditional-forwarder.html
    """

    parameter_display_string = """
    # directory-id : The directory ID for which to get the list of associated conditional forwarders.
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

    execute_one_parameter("ds", "describe-conditional-forwarders", "directory-id", add_option_dict)