#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/detach-instances-from-load-balancer.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # load-balancer-name : The name of the Lightsail load balancer.
    # instance-names : An array of strings containing the names of the instances you want to detach from the load balancer.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "detach-instances-from-load-balancer", "load-balancer-name", "instance-names", add_option_dict)
