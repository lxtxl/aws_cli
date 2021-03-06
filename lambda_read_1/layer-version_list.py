#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-layer-versions.html
if __name__ == '__main__':
    """
	delete-layer-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-layer-version.html
	get-layer-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version.html
	publish-layer-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html
    """

    parameter_display_string = """
    # layer-name : The name or Amazon Resource Name (ARN) of the layer.
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

    execute_one_parameter("lambda", "list-layer-versions", "layer-name", add_option_dict)