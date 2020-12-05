#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/allocate-static-ip.html
if __name__ == '__main__':
    """
	attach-static-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-static-ip.html
	detach-static-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/detach-static-ip.html
	get-static-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-static-ip.html
	get-static-ips : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-static-ips.html
	release-static-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/release-static-ip.html
    """

    parameter_display_string = """
    # static-ip-name : The name of the static IP address.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "allocate-static-ip", "static-ip-name", add_option_dict)





