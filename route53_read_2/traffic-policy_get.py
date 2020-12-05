#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-traffic-policy.html
if __name__ == '__main__':
    """
	create-traffic-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-traffic-policy.html
	delete-traffic-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-traffic-policy.html
	list-traffic-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policies.html
    """

    parameter_display_string = """
    # id : The ID of the traffic policy that you want to get information about.
    # traffic-policy-version : The version number of the traffic policy that you want to get information about.
    """

    execute_two_parameter("route53", "get-traffic-policy", "id", "traffic-policy-version", parameter_display_string)