#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-flow-logs.html
if __name__ == '__main__':
    """
	delete-flow-logs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-flow-logs.html
	describe-flow-logs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-flow-logs.html
    """

    parameter_display_string = """
    # resource-ids : The ID of the subnet, network interface, or VPC for which you want to create a flow log.
Constraints: Maximum of 1000 resources
(string)
    # resource-type : The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
Possible values:

VPC
Subnet
NetworkInterface
    # traffic-type : The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
Possible values:

ACCEPT
REJECT
ALL
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "create-flow-logs", "resource-ids", "resource-type", "traffic-type", add_option_dict)
