#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license-configuration.html
if __name__ == '__main__':
    """
	delete-license-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-license-configuration.html
	get-license-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-license-configuration.html
	list-license-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-license-configurations.html
	update-license-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/update-license-configuration.html
    """

    parameter_display_string = """
    # name : Name of the license configuration.
    # license-counting-type : Dimension used to track the license inventory.
Possible values:

vCPU
Instance
Core
Socket
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("license-manager", "create-license-configuration", "name", "license-counting-type", add_option_dict)
