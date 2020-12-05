#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policy-instances-by-policy.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # traffic-policy-id : The ID of the traffic policy for which you want to list traffic policy instances.
    # traffic-policy-version : The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by TrafficPolicyId .
    """

    execute_two_parameter("route53", "list-traffic-policy-instances-by-policy", "traffic-policy-id", "traffic-policy-version", parameter_display_string)