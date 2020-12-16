#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-rule-group.html
if __name__ == '__main__':
    """
	create-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-rule-group.html
	delete-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-rule-group.html
	list-rule-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-rule-groups.html
	update-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-rule-group.html
    """

    parameter_display_string = """
    # name : The name of the rule group. You cannot change the name of a rule group after you create it.
    # scope : Specifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an API Gateway REST API, or an AppSync GraphQL API.
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

CLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .
API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

CLOUDFRONT
REGIONAL
    """

    execute_two_parameter("wafv2", "get-rule-group", "name", "scope", parameter_display_string)