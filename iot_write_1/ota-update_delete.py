#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-ota-update.html
if __name__ == '__main__':
    """
	create-ota-update : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-ota-update.html
	get-ota-update : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-ota-update.html
	list-ota-updates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-ota-updates.html
    """

    parameter_display_string = """
    # ota-update-id : The ID of the OTA update to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "delete-ota-update", "ota-update-id", add_option_dict)





