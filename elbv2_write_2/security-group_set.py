#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-security-groups.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # load-balancer-arn : The Amazon Resource Name (ARN) of the load balancer.
    # security-groups : The IDs of the security groups.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elbv2", "set-security-groups", "load-balancer-arn", "security-groups", add_option_dict)
