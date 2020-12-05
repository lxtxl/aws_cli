#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/describe-registry.html
if __name__ == '__main__':
    """
	create-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/create-registry.html
	delete-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-registry.html
	list-registries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-registries.html
	update-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/update-registry.html
    """

    parameter_display_string = """
    # registry-name : The name of the registry.
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

    execute_one_parameter("schemas", "describe-registry", "registry-name", add_option_dict)