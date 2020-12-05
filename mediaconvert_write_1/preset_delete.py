#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-preset.html
if __name__ == '__main__':
    """
	create-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-preset.html
	get-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-preset.html
	list-presets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-presets.html
	update-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-preset.html
    """

    parameter_display_string = """
    # name : The name of the preset to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediaconvert", "delete-preset", "name", add_option_dict)





