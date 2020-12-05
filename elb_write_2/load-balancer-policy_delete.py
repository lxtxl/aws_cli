#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer-policy.html
if __name__ == '__main__':
    """
	create-load-balancer-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-policy.html
	describe-load-balancer-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-policies.html
    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer.
    # policy-name : The name of the policy.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elb", "delete-load-balancer-policy", "load-balancer-name", "policy-name", add_option_dict)
