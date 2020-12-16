#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-insights.html
if __name__ == '__main__':
    """
	create-insight : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-insight.html
	delete-insight : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-insight.html
	update-insight : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-insight.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("securityhub", "get-insights", add_option_dict)