#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-key-group.html
if __name__ == '__main__':
    """
	create-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-key-group.html
	delete-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-key-group.html
	list-key-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-key-groups.html
	update-key-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-key-group.html
    """

    parameter_display_string = """
    # id : The identifier of the key group that you are getting. To get the identifier, use ListKeyGroups .
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

    execute_one_parameter("cloudfront", "get-key-group", "id", add_option_dict)