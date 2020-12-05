#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policies.html
if __name__ == '__main__':
    """
	create-traffic-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-traffic-policy.html
	delete-traffic-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-traffic-policy.html
	get-traffic-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-traffic-policy.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("route53", "list-traffic-policies", add_option_dict)