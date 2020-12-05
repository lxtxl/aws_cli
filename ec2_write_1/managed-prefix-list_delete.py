#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-managed-prefix-list.html
if __name__ == '__main__':
    """
	create-managed-prefix-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-managed-prefix-list.html
	describe-managed-prefix-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-managed-prefix-lists.html
	modify-managed-prefix-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-managed-prefix-list.html
    """

    parameter_display_string = """
    # prefix-list-id : The ID of the prefix list.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-managed-prefix-list", "prefix-list-id", add_option_dict)





