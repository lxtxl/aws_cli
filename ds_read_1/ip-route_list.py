#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-ip-routes.html
if __name__ == '__main__':
    """
	add-ip-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/add-ip-routes.html
	remove-ip-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/remove-ip-routes.html
    """

    parameter_display_string = """
    # directory-id : Identifier (ID) of the directory for which you want to retrieve the IP addresses.
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

    execute_one_parameter("ds", "list-ip-routes", "directory-id", add_option_dict)