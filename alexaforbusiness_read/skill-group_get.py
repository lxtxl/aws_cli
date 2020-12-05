#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-skill-group.html
if __name__ == '__main__':
    """
	create-skill-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-skill-group.html
	delete-skill-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-skill-group.html
	search-skill-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-skill-groups.html
	update-skill-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-skill-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("alexaforbusiness", "get-skill-group", add_option_dict)