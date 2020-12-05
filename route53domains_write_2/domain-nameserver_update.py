#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/update-domain-nameservers.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # domain-name : The name of the domain that you want to change name servers for.
    # nameservers : A list of new name servers for the domain.
(structure)

Nameserver includes the following elements.
Name -> (string)

The fully qualified host name of the name server.
Constraint: Maximum 255 characters

GlueIps -> (list)

Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
Constraints: The list can contain only one IPv4 and one IPv6 address.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53domains", "update-domain-nameservers", "domain-name", "nameservers", add_option_dict)
