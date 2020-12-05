#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-key-groups.html
if __name__ == '__main__':
    """
	create-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-key-group.html
	delete-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-key-group.html
	get-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-key-group.html
	update-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-key-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("cloudfront", "list-key-groups", add_option_dict)