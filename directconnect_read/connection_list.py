#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-connections.html
if __name__ == '__main__':
    """
	confirm-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-connection.html
	create-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-connection.html
	delete-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-connection.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("directconnect", "describe-connections", add_option_dict)