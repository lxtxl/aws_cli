#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-vpc-peering-connections.html
if __name__ == '__main__':
    """
	create-vpc-peering-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-vpc-peering-connection.html
	delete-vpc-peering-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-vpc-peering-connection.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("gamelift", "describe-vpc-peering-connections", add_option_dict)