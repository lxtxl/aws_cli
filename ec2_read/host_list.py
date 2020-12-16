#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-hosts.html
if __name__ == '__main__':
    """
	allocate-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-hosts.html
	modify-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-hosts.html
	release-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/release-hosts.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ec2", "describe-hosts", add_option_dict)