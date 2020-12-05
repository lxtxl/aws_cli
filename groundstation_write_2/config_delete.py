#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/delete-config.html
if __name__ == '__main__':
    """
	create-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-config.html
	get-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-config.html
	list-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-configs.html
	update-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/update-config.html
    """

    parameter_display_string = """
    # config-id : UUID of a Config .
    # config-type : Type of a Config .
Possible values:

antenna-downlink
antenna-downlink-demod-decode
antenna-uplink
dataflow-endpoint
tracking
uplink-echo
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("groundstation", "delete-config", "config-id", "config-type", add_option_dict)
