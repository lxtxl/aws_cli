#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-nat-gateway.html
if __name__ == '__main__':
    """
	delete-nat-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-nat-gateway.html
	describe-nat-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-nat-gateways.html
    """

    parameter_display_string = """
    # allocation-id : The allocation ID of an Elastic IP address to associate with the NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it.
    # subnet-id : The subnet in which to create the NAT gateway.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-nat-gateway", "allocation-id", "subnet-id", add_option_dict)
