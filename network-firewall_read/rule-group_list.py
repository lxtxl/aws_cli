#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-rule-group.html
if __name__ == '__main__':
    """
	create-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-rule-group.html
	delete-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-rule-group.html
	list-rule-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-rule-groups.html
	update-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-rule-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("network-firewall", "describe-rule-group", add_option_dict)