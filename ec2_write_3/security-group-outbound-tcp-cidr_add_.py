#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/authorize-security-group-egress.html
if __name__ == '__main__':
    """
	delete-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-security-group.html
	describe-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html
    """

    parameter_display_string = """
    # --group-id : The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
    # --port : For TCP or UDP: The range of ports to allow. A single integer or a range (min-max ).
        For ICMP: A single integer or a range (type-code ) representing the ICMP type number and the ICMP code number respectively. A value of -1 indicates all ICMP codes for all ICMP types. A value of -1 just for type indicates all ICMP codes for the specified ICMP type.
    # --cidr : The CIDR IP range.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    add_option_dict["no_value_parameter_list"] = ["--protocol tcp"]
    write_three_parameter("ec2", "authorize-security-group-egress", "group-id", "port", "cidr", add_option_dict)

