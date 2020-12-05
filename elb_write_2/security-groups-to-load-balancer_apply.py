#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/apply-security-groups-to-load-balancer.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer.
    # security-groups : The IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elb", "apply-security-groups-to-load-balancer", "load-balancer-name", "security-groups", add_option_dict)
