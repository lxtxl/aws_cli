#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cache-policy.html
if __name__ == '__main__':
    """
	create-cache-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-cache-policy.html
	delete-cache-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-cache-policy.html
	get-cache-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cache-policy.html
	list-cache-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cache-policies.html
    """

    parameter_display_string = """
    # cache-policy-config : 
    # id : The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behaviorâs CachePolicyId field in the response to GetDistributionConfig .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudfront", "update-cache-policy", "cache-policy-config", "id", add_option_dict)
