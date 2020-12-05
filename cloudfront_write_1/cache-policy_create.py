#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-cache-policy.html
if __name__ == '__main__':
    """
	delete-cache-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-cache-policy.html
	get-cache-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cache-policy.html
	list-cache-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cache-policies.html
	update-cache-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cache-policy.html
    """

    parameter_display_string = """
    # cache-policy-config : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudfront", "create-cache-policy", "cache-policy-config", add_option_dict)





