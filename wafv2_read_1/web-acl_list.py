#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-web-acls.html
if __name__ == '__main__':
    """
	associate-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/associate-web-acl.html
	create-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-web-acl.html
	delete-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-web-acl.html
	disassociate-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/disassociate-web-acl.html
	get-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-web-acl.html
	update-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-web-acl.html
    """

    parameter_display_string = """
    # scope : Specifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an API Gateway REST API, or an AppSync GraphQL API.
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

CLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .
API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

CLOUDFRONT
REGIONAL
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("wafv2", "list-web-acls", "scope", add_option_dict)