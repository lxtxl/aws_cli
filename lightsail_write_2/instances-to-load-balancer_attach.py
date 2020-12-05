#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-instances-to-load-balancer.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer.
    # instance-names : An array of strings representing the instance name(s) you want to attach to your load balancer.
An instance must be running before you can attach it to your load balancer.
There are no additional limits on the number of instances you can attach to your load balancer, aside from the limit of Lightsail instances you can create in your account (20).
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "attach-instances-to-load-balancer", "load-balancer-name", "instance-names", add_option_dict)
