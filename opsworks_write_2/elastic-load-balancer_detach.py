#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/detach-elastic-load-balancer.html
if __name__ == '__main__':
    """
	attach-elastic-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/attach-elastic-load-balancer.html
	describe-elastic-load-balancers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-elastic-load-balancers.html
    """

    parameter_display_string = """
    # elastic-load-balancer-name : The Elastic Load Balancing instanceâs name.
    # layer-id : The ID of the layer that the Elastic Load Balancing instance is attached to.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks", "detach-elastic-load-balancer", "elastic-load-balancer-name", "layer-id", add_option_dict)
