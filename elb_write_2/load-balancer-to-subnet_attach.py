#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/attach-load-balancer-to-subnets.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer.
    # subnets : The IDs of the subnets to add. You can add only one subnet per Availability Zone.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elb", "attach-load-balancer-to-subnets", "load-balancer-name", "subnets", add_option_dict)