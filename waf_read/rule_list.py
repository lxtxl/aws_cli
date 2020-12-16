#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rules.html
if __name__ == '__main__':
    """
	create-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule.html
	delete-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rule.html
	get-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rule.html
	update-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("waf", "list-rules", add_option_dict)