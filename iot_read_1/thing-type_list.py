#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-type.html
if __name__ == '__main__':
    """
	create-thing-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-type.html
	delete-thing-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing-type.html
	deprecate-thing-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/deprecate-thing-type.html
	list-thing-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-types.html
    """

    parameter_display_string = """
    # thing-type-name : The name of the thing type.
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

    execute_one_parameter("iot", "describe-thing-type", "thing-type-name", add_option_dict)