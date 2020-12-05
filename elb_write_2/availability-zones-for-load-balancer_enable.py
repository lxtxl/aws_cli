#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/enable-availability-zones-for-load-balancer.html
if __name__ == '__main__':
    """
	disable-availability-zones-for-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/disable-availability-zones-for-load-balancer.html
    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer.
    # availability-zones : The Availability Zones. These must be in the same region as the load balancer.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elb", "enable-availability-zones-for-load-balancer", "load-balancer-name", "availability-zones", add_option_dict)
