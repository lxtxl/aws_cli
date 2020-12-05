#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-layer.html
if __name__ == '__main__':
    """
	create-layer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-layer.html
	describe-layers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-layers.html
	update-layer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-layer.html
    """

    parameter_display_string = """
    # layer-id : The layer ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("opsworks", "delete-layer", "layer-id", add_option_dict)





