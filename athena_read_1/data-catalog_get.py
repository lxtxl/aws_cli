#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-data-catalog.html
if __name__ == '__main__':
    """
	create-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html
	delete-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-data-catalog.html
	list-data-catalogs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-data-catalogs.html
	update-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-data-catalog.html
    """

    parameter_display_string = """
    # name : The name of the data catalog to return.
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

    execute_one_parameter("athena", "get-data-catalog", "name", add_option_dict)