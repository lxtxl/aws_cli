#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy-change-protection.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # firewall-policy-change-protection | --no-firewall-policy-change-protection : A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to TRUE .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("network-firewall", "update-firewall-policy-change-protection", "firewall-policy-change-protection | --no-firewall-policy-change-protection", add_option_dict)





