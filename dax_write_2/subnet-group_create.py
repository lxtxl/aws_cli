#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/create-subnet-group.html
if __name__ == '__main__':
    """
	delete-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-subnet-group.html
	describe-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-subnet-groups.html
	update-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/update-subnet-group.html
    """

    parameter_display_string = """
    # subnet-group-name : A name for the subnet group. This value is stored as a lowercase string.
    # subnet-ids : A list of VPC subnet IDs for the subnet group.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dax", "create-subnet-group", "subnet-group-name", "subnet-ids", add_option_dict)
