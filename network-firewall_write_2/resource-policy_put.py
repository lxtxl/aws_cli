#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/put-resource-policy.html
if __name__ == '__main__':
    """
	delete-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-resource-policy.html
	describe-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-resource-policy.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the account that you want to share rule groups and firewall policies with.
    # policy : The AWS Identity and Access Management policy statement that lists the accounts that you want to share your rule group or firewall policy with and the operations that you want the accounts to be able to perform.
For a rule group resource, you can specify the following operations in the Actions section of the statement:

network-firewall:CreateFirewallPolicy
network-firewall:UpdateFirewallPolicy
network-firewall:ListRuleGroups

For a firewall policy resource, you can specify the following operations in the Actions section of the statement:

network-firewall:CreateFirewall
network-firewall:UpdateFirewall
network-firewall:AssociateFirewallPolicy
network-firewall:ListFirewallPolicies

In the Resource section of the statement, you specify the ARNs for the rule groups and firewall policies that you want to share with the account that you specified in Arn .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("network-firewall", "put-resource-policy", "resource-arn", "policy", add_option_dict)
