#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-byte-match-sets.html
if __name__ == '__main__':
    """
	create-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-byte-match-set.html
	delete-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-byte-match-set.html
	get-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-byte-match-set.html
	update-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-byte-match-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("waf-regional", "list-byte-match-sets", add_option_dict)