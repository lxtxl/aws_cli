#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/deprovision-byoip-cidr.html
if __name__ == '__main__':
    """
	advertise-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/advertise-byoip-cidr.html
	list-byoip-cidrs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-byoip-cidrs.html
	provision-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/provision-byoip-cidr.html
	withdraw-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/withdraw-byoip-cidr.html
    """

    parameter_display_string = """
    # cidr : The address range, in CIDR notation. The prefix must be the same prefix that you specified when you provisioned the address range.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("globalaccelerator", "deprovision-byoip-cidr", "cidr", add_option_dict)





