#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-metric-filters.html
if __name__ == '__main__':
    """
	delete-metric-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-metric-filter.html
	put-metric-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-metric-filter.html
	test-metric-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/test-metric-filter.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("logs", "describe-metric-filters", add_option_dict)