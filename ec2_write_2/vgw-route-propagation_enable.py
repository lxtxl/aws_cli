#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-vgw-route-propagation.html
if __name__ == '__main__':
    """
	disable-vgw-route-propagation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vgw-route-propagation.html
    """

    parameter_display_string = """
    # gateway-id : The ID of the virtual private gateway that is attached to a VPC. The virtual private gateway must be attached to the same VPC that the routing tables are associated with.
    # route-table-id : The ID of the route table. The routing table must be associated with the same VPC that the virtual private gateway is attached to.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "enable-vgw-route-propagation", "gateway-id", "route-table-id", add_option_dict)
