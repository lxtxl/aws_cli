#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-portals.html
if __name__ == '__main__':
    """
	create-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-portal.html
	delete-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-portal.html
	describe-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-portal.html
	update-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-portal.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("iotsitewise", "list-portals", add_option_dict)