#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html
if __name__ == '__main__':
    """
	attach-load-balancer-tls-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-load-balancer-tls-certificate.html
	create-load-balancer-tls-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-load-balancer-tls-certificate.html
	delete-load-balancer-tls-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-load-balancer-tls-certificate.html
    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer you associated with your SSL/TLS certificate.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("lightsail", "get-load-balancer-tls-certificates", "load-balancer-name", add_option_dict)