#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-device-definition.html
if __name__ == '__main__':
    """
	create-device-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-device-definition.html
	delete-device-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-device-definition.html
	list-device-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-device-definitions.html
	update-device-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-device-definition.html
    """

    parameter_display_string = """
    # device-definition-id : The ID of the device definition.
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

    execute_one_parameter("greengrass", "get-device-definition", "device-definition-id", add_option_dict)