#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-byoip-cidrs.html
if __name__ == '__main__':
    """
	advertise-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/advertise-byoip-cidr.html
	deprovision-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deprovision-byoip-cidr.html
	provision-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/provision-byoip-cidr.html
	withdraw-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/withdraw-byoip-cidr.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ec2", "describe-byoip-cidrs", add_option_dict)