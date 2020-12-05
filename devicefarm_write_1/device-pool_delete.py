#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-device-pool.html
if __name__ == '__main__':
    """
	create-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-device-pool.html
	get-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-device-pool.html
	list-device-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-device-pools.html
	update-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-device-pool.html
    """

    parameter_display_string = """
    # arn : Represents the Amazon Resource Name (ARN) of the Device Farm device pool to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devicefarm", "delete-device-pool", "arn", add_option_dict)





