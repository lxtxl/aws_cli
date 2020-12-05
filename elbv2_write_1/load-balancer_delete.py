#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-load-balancer.html
if __name__ == '__main__':
    """
	create-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-load-balancer.html
	describe-load-balancers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-load-balancers.html
    """

    parameter_display_string = """
    # load-balancer-arn : The Amazon Resource Name (ARN) of the load balancer.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elbv2", "delete-load-balancer", "load-balancer-arn", add_option_dict)





