#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-connection.html
if __name__ == '__main__':
    """
	create-vpn-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html
	delete-vpn-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-connection.html
	describe-vpn-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-connections.html
    """

    parameter_display_string = """
    # vpn-connection-id : The ID of the VPN connection.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "modify-vpn-connection", "vpn-connection-id", add_option_dict)





