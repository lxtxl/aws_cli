#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-hosts.html
if __name__ == '__main__':
    """
	describe-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-hosts.html
	modify-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-hosts.html
	release-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/release-hosts.html
    """

    parameter_display_string = """
    # availability-zone : The Availability Zone in which to allocate the Dedicated Host.
    # quantity : The number of Dedicated Hosts to allocate to your account with these parameters.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "allocate-hosts", "availability-zone", "quantity", add_option_dict)
