#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-site.html
if __name__ == '__main__':
    """
	create-site : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-site.html
	get-sites : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-sites.html
	update-site : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-site.html
    """

    parameter_display_string = """
    # global-network-id : The ID of the global network.
    # site-id : The ID of the site.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("networkmanager", "delete-site", "global-network-id", "site-id", add_option_dict)
