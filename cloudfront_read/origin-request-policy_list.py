#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-origin-request-policies.html
if __name__ == '__main__':
    """
	create-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-origin-request-policy.html
	delete-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-origin-request-policy.html
	get-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-origin-request-policy.html
	update-origin-request-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-origin-request-policy.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("cloudfront", "list-origin-request-policies", add_option_dict)