#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-instance-attributes.html
if __name__ == '__main__':
    """
	describe-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-instance-attribute.html
	update-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-instance-attribute.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
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

    execute_one_parameter("connect", "list-instance-attributes", "instance-id", add_option_dict)