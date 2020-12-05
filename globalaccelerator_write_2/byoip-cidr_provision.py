#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/provision-byoip-cidr.html
if __name__ == '__main__':
    """
	advertise-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/advertise-byoip-cidr.html
	deprovision-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/deprovision-byoip-cidr.html
	list-byoip-cidrs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-byoip-cidrs.html
	withdraw-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/withdraw-byoip-cidr.html
    """

    parameter_display_string = """
    # cidr : The public IPv4 address range, in CIDR notation. The most specific IP prefix that you can specify is /24. The address range cannot overlap with another address range that youâve brought to this or another Region.
    # cidr-authorization-context : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("globalaccelerator", "provision-byoip-cidr", "cidr", "cidr-authorization-context", add_option_dict)
