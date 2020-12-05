#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-device-definition-version.html
if __name__ == '__main__':
    """
	get-device-definition-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-device-definition-version.html
	list-device-definition-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-device-definition-versions.html
    """

    parameter_display_string = """
    # device-definition-id : The ID of the device definition.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("greengrass", "create-device-definition-version", "device-definition-id", add_option_dict)





