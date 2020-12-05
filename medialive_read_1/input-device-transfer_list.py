#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-device-transfers.html
if __name__ == '__main__':
    """
	accept-input-device-transfer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/accept-input-device-transfer.html
	cancel-input-device-transfer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/cancel-input-device-transfer.html
	reject-input-device-transfer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/reject-input-device-transfer.html
    """

    parameter_display_string = """
    # transfer-type : Placeholder documentation for __string
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

    execute_one_parameter("medialive", "list-input-device-transfers", "transfer-type", add_option_dict)