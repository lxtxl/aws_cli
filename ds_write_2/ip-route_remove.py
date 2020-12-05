#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/remove-ip-routes.html
if __name__ == '__main__':
    """
	add-ip-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/add-ip-routes.html
	list-ip-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-ip-routes.html
    """

    parameter_display_string = """
    # directory-id : Identifier (ID) of the directory from which you want to remove the IP addresses.
    # cidr-ips : IP address blocks that you want to remove.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "remove-ip-routes", "directory-id", "cidr-ips", add_option_dict)
