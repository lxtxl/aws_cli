#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-dedicated-ip.html
if __name__ == '__main__':
    """
	get-dedicated-ips : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-dedicated-ips.html
    """

    parameter_display_string = """
    # ip : The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address thatâs assocaited with your Amazon Pinpoint account.
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

    execute_one_parameter("pinpoint-email", "get-dedicated-ip", "ip", add_option_dict)