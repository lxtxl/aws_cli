#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/accept-input-device-transfer.html
if __name__ == '__main__':
    """
	cancel-input-device-transfer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/cancel-input-device-transfer.html
	list-input-device-transfers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-device-transfers.html
	reject-input-device-transfer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/reject-input-device-transfer.html
    """

    parameter_display_string = """
    # input-device-id : The unique ID of the input device to accept. For example, hd-123456789abcdef.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("medialive", "accept-input-device-transfer", "input-device-id", add_option_dict)





