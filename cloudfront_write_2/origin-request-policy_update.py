#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-origin-request-policy.html
if __name__ == '__main__':
    """
	create-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-origin-request-policy.html
	delete-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-origin-request-policy.html
	get-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-origin-request-policy.html
	list-origin-request-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-origin-request-policies.html
    """

    parameter_display_string = """
    # origin-request-policy-config : 
    # id : The unique identifier for the origin request policy that you are updating. The identifier is returned in a cache behaviorâs OriginRequestPolicyId field in the response to GetDistributionConfig .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudfront", "update-origin-request-policy", "origin-request-policy-config", "id", add_option_dict)
