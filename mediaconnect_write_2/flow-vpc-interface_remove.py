#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/remove-flow-vpc-interface.html
if __name__ == '__main__':
    """
	add-flow-vpc-interfaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-vpc-interfaces.html
    """

    parameter_display_string = """
    # flow-arn : The flow that you want to remove a VPC interface from.
    # vpc-interface-name : The name of the VPC interface that you want to remove.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediaconnect", "remove-flow-vpc-interface", "flow-arn", "vpc-interface-name", add_option_dict)
