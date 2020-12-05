#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/put-resolver-rule-policy.html
if __name__ == '__main__':
    """
	get-resolver-rule-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule-policy.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the account that you want to share rules with.
    # resolver-rule-policy : An AWS Identity and Access Management policy statement that lists the rules that you want to share with another AWS account and the operations that you want the account to be able to perform. You can specify the following operations in the Actions section of the statement:

route53resolver:GetResolverRule
route53resolver:AssociateResolverRule
route53resolver:DisassociateResolverRule
route53resolver:ListResolverRules
route53resolver:ListResolverRuleAssociations

In the Resource section of the statement, you specify the ARNs for the rules that you want to share with the account that you specified in Arn .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53resolver", "put-resolver-rule-policy", "arn", "resolver-rule-policy", add_option_dict)
