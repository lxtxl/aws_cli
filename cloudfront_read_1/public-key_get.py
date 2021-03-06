#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-public-key.html
if __name__ == '__main__':
    """
	create-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-public-key.html
	delete-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-public-key.html
	list-public-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-public-keys.html
	update-public-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-public-key.html
    """

    parameter_display_string = """
    # id : The identifier of the public key you are getting.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("cloudfront", "get-public-key", "id", add_option_dict)