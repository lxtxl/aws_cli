#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/put-permission-policy.html
if __name__ == '__main__':
    """
	delete-permission-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-permission-policy.html
	get-permission-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-permission-policy.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the  RuleGroup to which you want to attach the policy.
    # policy : The policy to attach to the specified rule group.
The policy specifications must conform to the following:

The policy must be composed using IAM Policy version 2012-10-17 or version 2015-01-01.
The policy must include specifications for Effect , Action , and Principal .
Effect must specify Allow .
Action must specify wafv2:CreateWebACL , wafv2:UpdateWebACL , and wafv2:PutFirewallManagerRuleGroups . AWS WAF rejects any extra actions or wildcard actions in the policy.
The policy must not include a Resource parameter.

For more information, see IAM Policies .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("wafv2", "put-permission-policy", "resource-arn", "policy", add_option_dict)
