#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-streaming-distribution.html
if __name__ == '__main__':
    """
	create-streaming-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-streaming-distribution.html
	delete-streaming-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-streaming-distribution.html
	list-streaming-distributions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-streaming-distributions.html
	update-streaming-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-streaming-distribution.html
    """

    parameter_display_string = """
    # id : The streaming distributionâs ID.
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

    execute_one_parameter("cloudfront", "get-streaming-distribution", "id", add_option_dict)