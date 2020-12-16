#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-routing-profile-concurrency.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # routing-profile-id : The identifier of the routing profile.
    # media-concurrencies : The channels agents can handle in the Contact Control Panel (CCP).
(structure)

Contains information about which channels are supported, and how many contacts an agent can have on a channel simultaneously.
Channel -> (string)

The channels that agents can handle in the Contact Control Panel (CCP).

Concurrency -> (integer)

The number of contacts an agent can have on a channel simultaneously.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "update-routing-profile-concurrency", "instance-id", "routing-profile-id", "media-concurrencies", add_option_dict)
