#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-device-instance.html
if __name__ == '__main__':
    """
	list-device-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-device-instances.html
	update-device-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-device-instance.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the instance youâre requesting information about.
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

    execute_one_parameter("devicefarm", "get-device-instance", "arn", add_option_dict)