#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-firewall-policy.html
if __name__ == '__main__':
    """
	associate-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/associate-firewall-policy.html
	create-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-firewall-policy.html
	delete-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-firewall-policy.html
	list-firewall-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-firewall-policies.html
	update-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("network-firewall", "describe-firewall-policy", add_option_dict)