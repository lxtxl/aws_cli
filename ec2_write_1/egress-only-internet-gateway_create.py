#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-egress-only-internet-gateway.html
if __name__ == '__main__':
    """
	delete-egress-only-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-egress-only-internet-gateway.html
	describe-egress-only-internet-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-egress-only-internet-gateways.html
    """

    parameter_display_string = """
    # vpc-id : The ID of the VPC for which to create the egress-only internet gateway.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "create-egress-only-internet-gateway", "vpc-id", add_option_dict)





