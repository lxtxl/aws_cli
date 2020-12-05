#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-origin-request-policy.html
if __name__ == '__main__':
    """
	create-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-origin-request-policy.html
	delete-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-origin-request-policy.html
	list-origin-request-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-origin-request-policies.html
	update-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-origin-request-policy.html
    """

    parameter_display_string = """
    # id : The unique identifier for the origin request policy. If the origin request policy is attached to a distributionâs cache behavior, you can get the policyâs identifier using ListDistributions or GetDistribution . If the origin request policy is not attached to a cache behavior, you can get the identifier using ListOriginRequestPolicies .
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

    execute_one_parameter("cloudfront", "get-origin-request-policy", "id", add_option_dict)