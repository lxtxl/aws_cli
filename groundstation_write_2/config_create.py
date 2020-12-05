#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-config.html
if __name__ == '__main__':
    """
	delete-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/delete-config.html
	get-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-config.html
	list-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-configs.html
	update-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/update-config.html
    """

    parameter_display_string = """
    # config-data : 
    # name : Name of a Config .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("groundstation", "create-config", "config-data", "name", add_option_dict)
