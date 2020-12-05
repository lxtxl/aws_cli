#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/delete-preset.html
if __name__ == '__main__':
    """
	create-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/create-preset.html
	list-presets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-presets.html
	read-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/read-preset.html
    """

    parameter_display_string = """
    # id : The identifier of the preset for which you want to get detailed information.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elastictranscoder", "delete-preset", "id", add_option_dict)





