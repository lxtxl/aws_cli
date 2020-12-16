#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-security-keys.html
if __name__ == '__main__':
    """
	associate-security-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-security-key.html
	disassociate-security-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-security-key.html
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

    execute_one_parameter("connect", "list-security-keys", "instance-id", add_option_dict)