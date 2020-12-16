#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-studio-session-mappings.html
if __name__ == '__main__':
    """
	create-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-studio-session-mapping.html
	delete-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/delete-studio-session-mapping.html
	get-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/get-studio-session-mapping.html
	update-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/update-studio-session-mapping.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("emr", "list-studio-session-mappings", add_option_dict)