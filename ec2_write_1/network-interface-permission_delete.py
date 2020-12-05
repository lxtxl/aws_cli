#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-interface-permission.html
if __name__ == '__main__':
    """
	create-network-interface-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-interface-permission.html
	describe-network-interface-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interface-permissions.html
    """

    parameter_display_string = """
    # network-interface-permission-id : The ID of the network interface permission.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-network-interface-permission", "network-interface-permission-id", add_option_dict)





