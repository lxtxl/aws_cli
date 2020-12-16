#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-recommender-configurations.html
if __name__ == '__main__':
    """
	create-recommender-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-recommender-configuration.html
	delete-recommender-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-recommender-configuration.html
	get-recommender-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-recommender-configuration.html
	update-recommender-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-recommender-configuration.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("pinpoint", "get-recommender-configurations", add_option_dict)