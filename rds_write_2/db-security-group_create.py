#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-security-group.html
if __name__ == '__main__':
    """
	delete-db-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-security-group.html
	describe-db-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-security-groups.html
    """

    parameter_display_string = """
    # db-security-group-name : The name for the DB security group. This value is stored as a lowercase string.
Constraints:

Must be 1 to 255 letters, numbers, or hyphens.
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens
Must not be âDefaultâ

Example: mysecuritygroup
    # db-security-group-description : The description for the DB security group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "create-db-security-group", "db-security-group-name", "db-security-group-description", add_option_dict)
