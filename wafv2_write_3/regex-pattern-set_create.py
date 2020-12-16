#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-regex-pattern-set.html
if __name__ == '__main__':
    """
	delete-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-regex-pattern-set.html
	get-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-regex-pattern-set.html
	list-regex-pattern-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-regex-pattern-sets.html
	update-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-regex-pattern-set.html
    """

    parameter_display_string = """
    # name : The name of the set. You cannot change the name after you create the set.
    # scope : Specifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an API Gateway REST API, or an AppSync GraphQL API.
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

CLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .
API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

CLOUDFRONT
REGIONAL
    # regular-expression-list : Array of regular expression strings.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A single regular expression. This is used in a  RegexPatternSet .
RegexString -> (string)

The string representing the regular expression.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("wafv2", "create-regex-pattern-set", "name", "scope", "regular-expression-list", add_option_dict)
