#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/associate-firewall-policy.html
if __name__ == '__main__':
    """
	create-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-firewall-policy.html
	delete-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-firewall-policy.html
	describe-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-firewall-policy.html
	list-firewall-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-firewall-policies.html
	update-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy.html
    """

    parameter_display_string = """
    # firewall-policy-arn : The Amazon Resource Name (ARN) of the firewall policy.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("network-firewall", "associate-firewall-policy", "firewall-policy-arn", add_option_dict)





