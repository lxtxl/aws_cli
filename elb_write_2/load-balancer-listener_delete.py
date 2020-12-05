#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer-listeners.html
if __name__ == '__main__':
    """
	create-load-balancer-listeners : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-listeners.html
    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer.
    # load-balancer-ports : The client port numbers of the listeners.
(integer)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elb", "delete-load-balancer-listeners", "load-balancer-name", "load-balancer-ports", add_option_dict)
