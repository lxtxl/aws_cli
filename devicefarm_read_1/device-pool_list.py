#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-device-pools.html
if __name__ == '__main__':
    """
	create-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-device-pool.html
	delete-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-device-pool.html
	get-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-device-pool.html
	update-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-device-pool.html
    """

    parameter_display_string = """
    # arn : The project ARN.
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

    execute_one_parameter("devicefarm", "list-device-pools", "arn", add_option_dict)