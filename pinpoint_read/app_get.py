#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-apps.html
if __name__ == '__main__':
    """
	create-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-app.html
	delete-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-app.html
	get-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-app.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("pinpoint", "get-apps", add_option_dict)