#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-load-balancer.html
if __name__ == '__main__':
    """
	create-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-load-balancer.html
	get-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer.html
	get-load-balancers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html
    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "delete-load-balancer", "load-balancer-name", add_option_dict)





