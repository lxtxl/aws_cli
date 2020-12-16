#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-memberships.html
if __name__ == '__main__':
    """
	create-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel-membership.html
	delete-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-membership.html
	describe-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-membership.html
    """

    parameter_display_string = """
    # channel-arn : The maximum number of channel memberships that you want returned.
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

    execute_one_parameter("chime", "list-channel-memberships", "channel-arn", add_option_dict)