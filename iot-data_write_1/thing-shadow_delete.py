#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/delete-thing-shadow.html
if __name__ == '__main__':
    """
	get-thing-shadow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/get-thing-shadow.html
	update-thing-shadow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/update-thing-shadow.html
    """

    parameter_display_string = """
    # thing-name : The name of the thing.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot-data", "delete-thing-shadow", "thing-name", add_option_dict)





