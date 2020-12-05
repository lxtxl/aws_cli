#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-geo-match-sets.html
if __name__ == '__main__':
    """
	create-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-geo-match-set.html
	delete-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-geo-match-set.html
	get-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-geo-match-set.html
	update-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-geo-match-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("waf", "list-geo-match-sets", add_option_dict)