#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-policies-for-backend-server.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer.
    # instance-port : The port number associated with the EC2 instance.
    # policy-names : The names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("elb", "set-load-balancer-policies-for-backend-server", "load-balancer-name", "instance-port", "policy-names", add_option_dict)
