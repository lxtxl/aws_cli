#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-rule-group.html
if __name__ == '__main__':
    """
	delete-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-rule-group.html
	describe-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-rule-group.html
	list-rule-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-rule-groups.html
	update-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-rule-group.html
    """

    parameter_display_string = """
    # rule-group-name : The descriptive name of the rule group. You canât change the name of a rule group after you create it.
    # type : Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.
Possible values:

STATELESS
STATEFUL
    # capacity : The maximum operating resources that this rule group can use. Rule group capacity is fixed at creation. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group.
You can retrieve the capacity that would be required for a rule group before you create the rule group by calling  CreateRuleGroup with DryRun set to TRUE .

Note

You canât change or exceed this capacity when you update the rule group, so leave room for your rule group to grow.

Capacity for a stateless rule group

For a stateless rule group, the capacity required is the sum of the capacity requirements of the individual rules that you expect to have in the rule group.
To calculate the capacity requirement of a single rule, multiply the capacity requirement values of each of the ruleâs match settings:

A match setting with no criteria specified has a value of 1.
A match setting with Any specified has a value of 1.
All other match settings have a value equal to the number of elements provided in the setting. For example, a protocol setting [âUDPâ] and a source setting [â10.0.0.0/24â] each have a value of 1. A protocol setting [âUDPâ,âTCPâ] has a value of 2. A source setting [â10.0.0.0/24â,â10.0.0.1/24â,â10.0.0.2/24â] has a value of 3.

A rule with no criteria specified in any of its match settings has a capacity requirement of 1. A rule with protocol setting [âUDPâ,âTCPâ], source setting [â10.0.0.0/24â,â10.0.0.1/24â,â10.0.0.2/24â], and a single specification or no specification for each of the other match settings has a capacity requirement of 6.

Capacity for a stateful rule group

For a stateful rule group, the minimum capacity required is the number of individual rules that you expect to have in the rule group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("network-firewall", "create-rule-group", "rule-group-name", "type", "capacity", add_option_dict)
