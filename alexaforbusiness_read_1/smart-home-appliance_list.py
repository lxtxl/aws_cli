#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-smart-home-appliances.html
if __name__ == '__main__':
    """
	forget-smart-home-appliances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/forget-smart-home-appliances.html
    """

    parameter_display_string = """
    # room-arn : The room that the appliances are associated with.
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

    execute_one_parameter("alexaforbusiness", "list-smart-home-appliances", "room-arn", add_option_dict)