#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-device-instance.html
if __name__ == '__main__':
    """
	get-device-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-device-instance.html
	list-device-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-device-instances.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the device instance.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devicefarm", "update-device-instance", "arn", add_option_dict)





