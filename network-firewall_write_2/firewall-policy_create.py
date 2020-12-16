#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-firewall-policy.html
if __name__ == '__main__':
    """
	associate-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/associate-firewall-policy.html
	delete-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-firewall-policy.html
	describe-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-firewall-policy.html
	list-firewall-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-firewall-policies.html
	update-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy.html
    """

    parameter_display_string = """
    # firewall-policy-name : The descriptive name of the firewall policy. You canât change the name of a firewall policy after you create it.
    # firewall-policy : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("network-firewall", "create-firewall-policy", "firewall-policy-name", "firewall-policy", add_option_dict)
