#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-connector-definition-versions.html
if __name__ == '__main__':
    """
	create-connector-definition-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-connector-definition-version.html
	get-connector-definition-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-connector-definition-version.html
    """

    parameter_display_string = """
    # connector-definition-id : The ID of the connector definition.
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

    execute_one_parameter("greengrass", "list-connector-definition-versions", "connector-definition-id", add_option_dict)