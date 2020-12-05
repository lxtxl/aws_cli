#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/add-ip-routes.html
if __name__ == '__main__':
    """
	list-ip-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-ip-routes.html
	remove-ip-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/remove-ip-routes.html
    """

    parameter_display_string = """
    # directory-id : Identifier (ID) of the directory to which to add the address block.
    # ip-routes : IP address blocks, using CIDR format, of the traffic to route. This is often the IP address block of the DNS server used for your on-premises domain.
(structure)

IP address block. This is often the address block of the DNS server used for your on-premises domain.
CidrIp -> (string)

IP address block using CIDR format, for example 10.0.0.0/24. This is often the address block of the DNS server used for your on-premises domain. For a single IP address use a CIDR address block with /32. For example 10.0.0.0/32.

Description -> (string)

Description of the address block.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "add-ip-routes", "directory-id", "ip-routes", add_option_dict)
