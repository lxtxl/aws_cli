#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-configs.html
if __name__ == '__main__':
    """
	create-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-config.html
	delete-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/delete-config.html
	get-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-config.html
	update-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/update-config.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("groundstation", "list-configs", add_option_dict)