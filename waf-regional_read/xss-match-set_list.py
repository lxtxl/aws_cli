#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-xss-match-sets.html
if __name__ == '__main__':
    """
	create-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-xss-match-set.html
	delete-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-xss-match-set.html
	get-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-xss-match-set.html
	update-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-xss-match-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("waf-regional", "list-xss-match-sets", add_option_dict)