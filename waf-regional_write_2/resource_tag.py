#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.
    # tags : (structure)


Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


A tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to âcustomerâ and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.
Tagging is only available through the API, SDKs, and CLI. You canât manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.
Key -> (string)
Value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf-regional", "tag-resource", "resource-arn", "tags", add_option_dict)
