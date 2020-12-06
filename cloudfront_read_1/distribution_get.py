#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-distribution.html
if __name__ == '__main__':
    """
	create-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-distribution.html
	delete-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-distribution.html
	list-distributions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distributions.html
	update-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-distribution.html
    """

    parameter_display_string = """
    # id : The distributionâs ID. If the ID is empty, an empty distribution configuration is returned.
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

    read_one_parameter("cloudfront", "get-distribution", "id", add_option_dict)