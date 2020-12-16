#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-acl-entry.html
if __name__ == '__main__':
    """
	create-network-acl-entry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl-entry.html
	replace-network-acl-entry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-network-acl-entry.html
    """

    parameter_display_string = """
    # egress | --ingress : Indicates whether the rule is an egress rule.
    # network-acl-id : The ID of the network ACL.
    # rule-number : The rule number of the entry to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "delete-network-acl-entry", "egress | --ingress", "network-acl-id", "rule-number", add_option_dict)
