#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html
if __name__ == '__main__':
    """
	delete-vpc : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc.html
	describe-vpcs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpcs.html
    """

    parameter_display_string = """
    # cidr-block : The IPv4 network range for the VPC, in CIDR notation. For example, 10.0.0.0/16 . We modify the specified CIDR block to its canonical form; for example, if you specify 100.68.0.18/18 , we modify it to 100.68.0.0/18 .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "create-vpc", "cidr-block", add_option_dict)





