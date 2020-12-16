#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-network-interface.html
if __name__ == '__main__':
    """
	create-network-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-interface.html
	delete-network-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-interface.html
	describe-network-interfaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interfaces.html
	detach-network-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-network-interface.html
    """

    parameter_display_string = """
    # device-index : The index of the device for the network interface attachment.
    # instance-id : The ID of the instance.
    # network-interface-id : The ID of the network interface.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "attach-network-interface", "device-index", "instance-id", "network-interface-id", add_option_dict)
