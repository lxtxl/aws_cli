#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-rule.html
if __name__ == '__main__':
    """
	create-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-rule.html
	delete-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-rule.html
	disassociate-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-rule.html
	get-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule.html
	list-resolver-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rules.html
	update-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-rule.html
    """

    parameter_display_string = """
    # resolver-rule-id : The ID of the Resolver rule that you want to associate with the VPC. To list the existing Resolver rules, use ListResolverRules .
    # vpc-id : The ID of the VPC that you want to associate the Resolver rule with.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53resolver", "associate-resolver-rule", "resolver-rule-id", "vpc-id", add_option_dict)
