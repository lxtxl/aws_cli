#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-network-interface-attribute.html
if __name__ == '__main__':
    """
	describe-network-interface-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interface-attribute.html
	modify-network-interface-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-network-interface-attribute.html
    """

    parameter_display_string = """
    # network-interface-id : The ID of the network interface.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "reset-network-interface-attribute", "network-interface-id", add_option_dict)





