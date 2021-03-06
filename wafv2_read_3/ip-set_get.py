#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-ip-set.html
if __name__ == '__main__':
    """
	create-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-ip-set.html
	delete-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-ip-set.html
	list-ip-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-ip-sets.html
	update-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-ip-set.html
    """

    parameter_display_string = """
    # name : The name of the IP set. You cannot change the name of an IPSet after you create it.
    # scope : Specifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an API Gateway REST API, or an AppSync GraphQL API.
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

CLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .
API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

CLOUDFRONT
REGIONAL
    """

    execute_two_parameter("wafv2", "get-ip-set", "name", "scope", parameter_display_string)