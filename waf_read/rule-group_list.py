#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rule-groups.html
if __name__ == '__main__':
    """
	create-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule-group.html
	delete-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rule-group.html
	get-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rule-group.html
	update-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("waf", "list-rule-groups", add_option_dict)