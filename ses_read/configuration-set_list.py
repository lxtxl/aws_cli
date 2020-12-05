#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-configuration-sets.html
if __name__ == '__main__':
    """
	create-configuration-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-configuration-set.html
	delete-configuration-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-configuration-set.html
	describe-configuration-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-configuration-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("ses", "list-configuration-sets", add_option_dict)