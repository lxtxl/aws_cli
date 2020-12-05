#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-load-balancer-tls-certificate.html
if __name__ == '__main__':
    """
	attach-load-balancer-tls-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-load-balancer-tls-certificate.html
	create-load-balancer-tls-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-load-balancer-tls-certificate.html
	get-load-balancer-tls-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html
    """

    parameter_display_string = """
    # load-balancer-name : The load balancer name.
    # certificate-name : The SSL/TLS certificate name.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "delete-load-balancer-tls-certificate", "load-balancer-name", "certificate-name", add_option_dict)
