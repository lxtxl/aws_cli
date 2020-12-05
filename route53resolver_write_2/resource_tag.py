#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) for the resource that you want to add tags to. To get the ARN for a resource, use the applicable Get or List command:

GetResolverEndpoint
GetResolverRule
GetResolverRuleAssociation
ListResolverEndpoints
ListResolverRuleAssociations
ListResolverRules
    # tags : The tags that you want to add to the specified resource.
(structure)

One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .
Key -> (string)

The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .

Value -> (string)

The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that youâre creating the resource for.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53resolver", "tag-resource", "resource-arn", "tags", add_option_dict)
