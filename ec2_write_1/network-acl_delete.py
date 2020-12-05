#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-acl.html
if __name__ == '__main__':
    """
	create-network-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl.html
	describe-network-acls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-acls.html
    """

    parameter_display_string = """
    # network-acl-id : The ID of the network ACL.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-network-acl", "network-acl-id", add_option_dict)





