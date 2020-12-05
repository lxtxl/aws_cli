#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/provision-byoip-cidr.html
if __name__ == '__main__':
    """
	advertise-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/advertise-byoip-cidr.html
	deprovision-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deprovision-byoip-cidr.html
	describe-byoip-cidrs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-byoip-cidrs.html
	withdraw-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/withdraw-byoip-cidr.html
    """

    parameter_display_string = """
    # cidr : The public IPv4 or IPv6 address range, in CIDR notation. The most specific IPv4 prefix that you can specify is /24. The most specific IPv6 prefix you can specify is /56. The address range cannot overlap with another address range that youâve brought to this or another Region.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "provision-byoip-cidr", "cidr", add_option_dict)





