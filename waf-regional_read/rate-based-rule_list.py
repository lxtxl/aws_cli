#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-rate-based-rules.html
if __name__ == '__main__':
    """
	create-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-rate-based-rule.html
	delete-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-rate-based-rule.html
	get-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-rate-based-rule.html
	update-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-rate-based-rule.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("waf-regional", "list-rate-based-rules", add_option_dict)