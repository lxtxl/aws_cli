#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer.html
if __name__ == '__main__':
    """
	create-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer.html
	describe-load-balancers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancers.html
    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elb", "delete-load-balancer", "load-balancer-name", add_option_dict)





