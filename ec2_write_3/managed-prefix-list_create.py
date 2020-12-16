#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-managed-prefix-list.html
if __name__ == '__main__':
    """
	delete-managed-prefix-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-managed-prefix-list.html
	describe-managed-prefix-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-managed-prefix-lists.html
	modify-managed-prefix-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-managed-prefix-list.html
    """

    parameter_display_string = """
    # prefix-list-name : A name for the prefix list.
Constraints: Up to 255 characters in length. The name cannot start with com.amazonaws .
    # max-entries : The maximum number of entries for the prefix list.
    # address-family : The IP address type.
Valid Values: IPv4 | IPv6
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "create-managed-prefix-list", "prefix-list-name", "max-entries", "address-family", add_option_dict)
