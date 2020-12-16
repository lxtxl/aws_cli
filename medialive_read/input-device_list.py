#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-devices.html
if __name__ == '__main__':
    """
	describe-input-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-input-device.html
	transfer-input-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/transfer-input-device.html
	update-input-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-input-device.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("medialive", "list-input-devices", add_option_dict)